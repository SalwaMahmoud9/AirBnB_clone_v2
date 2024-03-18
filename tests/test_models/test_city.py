#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instance(unittest.TestCase):
    """Unittest City class."""

    def test_city_instance(self):
        self.assertEqual(City, type(City()))

    def test_id_is_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_str(self):
        self.assertEqual(str, type(City().updated_at))

    def test_name_is_str(self):
        self.assertEqual(str, type(City().updated_at))

    def test_uniqueIds(self):
        model1 = City()
        model2 = City()
        self.assertNotEqual(model1.id, model2.id)

    def test_diff_created_at(self):
        model1 = City()
        sleep(1)
        model2 = City()
        self.assertLess(model1.created_at, model2.created_at)

    def test_diff_updated_at(self):
        model1 = City()
        sleep(1)
        model2 = City()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_storage_new(self):
        self.assertIn(City(), models.storage.all().values())

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        model = City()
        model.id = "100000"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[City] (100000)", modelstr)
        self.assertIn("'id': '100000'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestCity_save(unittest.TestCase):
    """Unittests save City class."""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        model = City()
        sleep(1)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_more_saves(self):
        model1 = City()
        sleep(1)
        updated_at1 = model1.updated_at
        model1.save()
        updated_at2 = model1.updated_at
        self.assertLess(updated_at1, updated_at2)
        sleep(1)
        model1.save()
        self.assertLess(updated_at2, model1.updated_at)

    def test_update_file(self):
        model = City()
        model.save()
        modelId = "City." + model.id
        with open("file.json", "r") as f:
            self.assertIn(modelId, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests to_dict City class."""

    def test_to_dict_type(self):
        model = City()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_correct_data(self):
        model = City()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_to_dict(self):
        model = City()
        model.name = "name"
        model.age = 100
        self.assertEqual("name", model.name)
        self.assertIn("age", model.to_dict())


if __name__ == "__main__":
    unittest.main()
