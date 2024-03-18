#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instance(unittest.TestCase):
    """Unittest Place class."""

    def test_place_instance(self):
        self.assertEqual(Place, type(Place()))

    def test_id_is_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_str(self):
        self.assertEqual(str, type(Place().city_id))

    def test_user_id_is_str(self):
        self.assertEqual(str, type(Place().user_id))

    def test_name_is_str(self):
        self.assertEqual(str, type(Place().name))

    def test_description_is_str(self):
        self.assertEqual(str, type(Place().description))

    def test_number_rooms_id_is_int(self):
        self.assertEqual(int, type(Place().number_rooms))

    def test_number_bathrooms_id_is_int(self):
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_max_guest_is_int(self):
        self.assertEqual(int, type(Place().max_guest))

    def test_price_by_night_is_int(self):
        self.assertEqual(int, type(Place().price_by_night))

    def test_latitude_is_int(self):
        self.assertEqual(float, type(Place().latitude))

    def test_longitude_is_int(self):
        self.assertEqual(float, type(Place().longitude))

    def test_amenity_ids_is_int(self):
        self.assertEqual(list, type(Place().amenity_ids))

    def test_uniqueIds(self):
        model1 = Place()
        model2 = Place()
        self.assertNotEqual(model1.id, model2.id)

    def test_diff_created_at(self):
        model1 = Place()
        sleep(1)
        model2 = Place()
        self.assertLess(model1.created_at, model2.created_at)

    def test_diff_updated_at(self):
        model1 = Place()
        sleep(1)
        model2 = Place()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_storage_new(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        model = Place()
        model.id = "100000"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[Place] (100000)", modelstr)
        self.assertIn("'id': '100000'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)


class TestPlace_save(unittest.TestCase):
    """Unittests save Place class."""
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
        model = Place()
        sleep(1)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_more_saves(self):
        model1 = Place()
        sleep(1)
        updated_at1 = model1.updated_at
        model1.save()
        updated_at2 = model1.updated_at
        self.assertLess(updated_at1, updated_at2)
        sleep(1)
        model1.save()
        self.assertLess(updated_at2, model1.updated_at)

    def test_update_file(self):
        model = Place()
        model.save()
        modelId = "Place." + model.id
        with open("file.json", "r") as f:
            self.assertIn(modelId, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests to_dict Place class."""

    def test_to_dict_type(self):
        model = Place()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_correct_data(self):
        model = Place()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_to_dict(self):
        model = Place()
        model.name = "name"
        model.age = 100
        self.assertEqual("name", model.name)
        self.assertIn("age", model.to_dict())


if __name__ == "__main__":
    unittest.main()
