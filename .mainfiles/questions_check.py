#!/usr/bin/python3

from models import storage
from models.metadata import Metadata
from models.questions import Question
from sys import exit


polls = storage.all("Poll")
questions = storage.all("Question")

if polls:
    poll = polls[0]

if not poll:
    print("no poll found")
    exit(1)


qcount_b4 = len(questions)
print("+++++++++++[Creating Question]++++++++++++")
q1 = Question(
    poll_id=poll.id, title="Which do you choose?",
    runner_text="allows multiple choice",
)
q1.save()
qcount_af = len(storage.all("Question"))
print(f"\t Success -> {q1.id}")
print("\t Check question in storage -> {}".format(
    all([storage.get("Question", q1.id) is not None,
         qcount_af == qcount_b4 + 1]))
)
print("+++++++++++[Creating Question Metadata]+++++++++++++")
qmd_len_b = len(q1.meta_data)
mdata = Metadata(name=f"question-{q1.serial}-meta",
                 owner_id=q1.id, owner_type="question",
                 use_as="question_img", mime_type="image/jpg",
                 location="/question/md/location")
if not mdata:
    print("\Failure -> couldn't create metadata")
    exit(1)

mdata.save()
print(f"\t Success -> {mdata.id}")
print("\t Check Metadata in storage and question is owner -> {}".format(
    all([(md := storage.get("Metadata", mdata.id)) is not None,
         md.owner_id == q1.id])))
print("\t Check Metadata in questions' metadata -> {}".format(
    all([mdata in q1.meta_data, qmd_len_b == len(q1.meta_data) - 1])))

print("+++++++++++[Create Option]+++++++++++++")



