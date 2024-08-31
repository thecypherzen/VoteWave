#!/usr/bin/python3

from datetime import datetime, timedelta
from models.base_class import Base, BaseClass
from uuid import uuid4
import unittest

class TestBaseClass(unittest.TestCase):
    """test the baseclasss"""

    def test_blank_create(self):
        newbase = BaseClass()
        with self.subTest("has id"):
            self.assertIsNotNone(getattr(newbase, "id"))
        with self.subTest("has created_at"):
            self.assertIsNotNone(getattr(newbase, "created_at"))
        with self.subTest("has updated_at"):
            self.assertIsNotNone(getattr(newbase, "updated_at"))
        with self.subTest("created_at == updated_at"):
            self.assertTrue(newbase.created_at == newbase.updated_at)
        with self.subTest("verify is baseclass"):
            self.assertTrue(newbase.__class__.__name__ == "BaseClass")

    def test_create_values(self):
        uid = str(uuid4()).replace("-", "")
        created = datetime.utcnow()
        updated = datetime.utcnow() + timedelta(hours=1, minutes=5)
        newbase = BaseClass(id=uid, created_at=created, updated_at=updated)
        with self.subTest("check uids match"):
            self.assertEqual(uid, newbase.id)
        with self.subTest("check created_at match"):
            self.assertEqual(created, newbase.created_at)
        with self.subTest("check updated_at match"):
            self.assertEqual(updated, newbase.updated_at)

    def test_to_dict(self):
        base = BaseClass()
        base_dict = base.to_dict()
        newbase = BaseClass(**base_dict)
        with self.subTest("check ids match"):
            self.assertEqual(base.id, newbase.id)
        with self.subTest("created_at match check"):
            self.assertEqual(base.created_at, newbase.created_at)
        with self.subTest("updated_at match check"):
            self.assertEqual(base.updated_at, newbase.updated_at)
        with self.subTest("check return type"):
            self.assertIsInstance(base_dict, dict)
        with self.subTest("check key __class__ exists"):
            self.assertTrue("__class__" in base_dict.keys())
        with self.subTest("check __class__ value is BaseClass"):
            self.assertEqual(base_dict.get("__class__"), "BaseClass")
