#!/usr/bin/python3
"""Defines the users view """

from api.v1.views import app_views
from flask import json, abort, redirect, request, Response, \
    send_from_directory, url_for
from models import storage
from models.users import User
from models.metadata import Metadata
from os import getenv, path
from pathlib import Path


# get a user
@app_views.route("/users/<string:user_id>", strict_slashes=False)
def user_details(user_id):
    """Returns details of a user by Id if
    found else 404
    """
    session = storage.session()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        abort(404)

    # get user's extra information
    user_dict = user.to_dict()

    own_activities = user.polls + user.elections
    user_dict["own_activites"] = [act.to_dict() for act in own_activities]
    user_dict["admin_of"] = [
        ad.to_dict() for ad in user.admin_of]
    user_dict["ivs_sent"] = [
        iv.to_dict() for iv in user.ivs_sent]
    user_dict["ivs_in"] = [
        iv.to_dict() for iv in user.ivs_received]
    user_dict["reviews"] = [rv.to_dict() for rv in user.reviews]
    user_dict["waitlists"] = [
        wl.to_dict() for wl in user.waitlists]
    user_dict["meta_data"] = [
        md.to_dict() for md in user._metadata]
    res = json.dumps(user_dict, indent=2) + '\n'
    return Response(res, mimetype="application/json")


# create a new user
@app_views.route("users/new", methods=["POST"],
                 strict_slashes=False)
def create_new_user():
    if not any([request.form,
                first_name := request.form.get("first_name"),
                email := request.form.get("email"),
                dob := request.form.get("dob"),
                password := request.form.get("password"),
                security_key := request.form.get("security_key"),
                request.files, avatar := request.files.get("avatar")]):
        res = json.dumps({"error": "Paylong missing some data",
                          "context": str(e)})
        abort(400, description=res)
    last_name = request.form.get("last_name") or ""
    username = request.form.get("username") or ""
    session = storage.session()
    existing_user = User.find_by_info(email=email, username=username)
    if existing_user:
         abort(403, description=json.dumps(
                 {"error": "Some values already \
                  used by another user", "context": {
                       "email": existing_user.email == email,
                       "username": existing_user.username == username
                  }}))

    base_path = getenv("VW_ROOT_PATH")

    # initialize user instance
    new_user = User(
        first_name=first_name, last_name=last_name,
        password=password, security_key=security_key,
        dob=dob, email=email, username=username
    )
    try:
        session.add(new_user)
        session.commit()
    except Exception as e:
            abort(500, description=json.dumps(
                 {"error": "An error occured while \
                  onboardig user", "context": str(e)}))

    # create user location
    user_path = path.join(base_path, "users", new_user.id)
    Path(user_path).mkdir(parents=True, exist_ok=True)

    # create metadata
    user_meta = Metadata(
         owner_id=new_user.id, mime_type=avatar.mimetype,
         use_as="avatar", location="default", owner_type="user",
         name=avatar.filename
    )
    try:
         session.add(user_meta)
         session.commit()
    except Exception as e:
         print(str(e))
         abort(500, description=json.dumps(
              {"error": "An error occured while \
               onboardig user", "context": str(e)}))

    # save avatar
    meta_path = path.join(user_path, "metadata")
    Path(meta_path).mkdir(parents=True, exist_ok=True)
    avatar_path = path.join(meta_path, user_meta.id)
    avatar.save(avatar_path)

    print("NEW USER CREATED SUCCESSFULLY")

    res_msg = {
         "user_id": f"{new_user.id}",
         "avatar_id": f"{user_meta.id}"
    }
    res = json.dumps(res_msg, indent=2) + '\n'
    session.close()
    return Response(res, mimetype="application/json",  status=200)

# get user's avatar
@app_views.route("/users/<string:user_id>/avatar")
def user_avatar(user_id):
     user = storage.get("User", user_id)
     if not user:
          abort(404)
     user_meta = user._metadata
     if not user_meta:
          abort(404)
     filtered = list(filter(lambda item: item.use_as == "avatar", user_meta))
     if not filtered:
          abort(404)
     meta_id = filtered[0].id
     folder = path.join(getenv('VW_ROOT_PATH'), "users",
                        f"{user_id}", "metadata")
     filepath = path.join(folder, f"{meta_id}")
     if not path.exists(filepath):
          abort(404)

     return send_from_directory(folder, meta_id,
                                mimetype=filtered[0].mime_type)