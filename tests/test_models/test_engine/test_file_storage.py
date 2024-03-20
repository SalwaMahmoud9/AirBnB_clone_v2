#!/usr/bin/python3
""" test_fileStorage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'fileStorage test not supported')
class test_fileStorage(unittest.TestCase):
    """test_fileStorage"""

    def setUp(self):
        """test_fileStorage"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """test_fileStorage"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """test_fileStorage"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """test_fileStorage"""
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """test_fileStorage"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """test_fileStorage"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """test_fileStorage"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """test_fileStorage"""
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """test_fileStorage"""
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """test_fileStorage"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """test_fileStorage"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """test_fileStorage"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """test_fileStorage"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """test_fileStorage"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """test_fileStorage"""
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """test_fileStorage"""
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
