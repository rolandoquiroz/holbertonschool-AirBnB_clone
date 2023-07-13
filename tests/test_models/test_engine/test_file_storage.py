#!/usr/bin/python3

"""

This module define a TestFileStorage Class

"""

import unittest
from time import time
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel



class TestFileStorage(unittest.TestCase):
    """
    A TestFileStorage Class
    """

    def setUp(self):
        self.strg = FileStorage()
        self.bmdl = BaseModel()
        self.start = time()

    def tearDown(self):
        self.end = time()
    
    def test_file_path(self): 
        self.assertEqual(self.strg._FileStorage__file_path, 'file.json')

    def test_objects(self):
        self.assertEqual(self.strg._FileStorage__objects, {})

    def test_all(self):
        self.assertEqual(self.strg.all(), {})

    def test_new(self):
        self.strg.new(self.bmdl)
        self.assertDictEqual(self.strg.all(), 
                             {f'BaseModel.{self.bmdl.id}': self.bmdl})
        self.strg.all().clear()
    
    def test_save(self):
        self.strg.new(self.bmdl)
        self.strg.save()

        with open('file.json', 'r') as f:
            json_obj = json.loads(f.read())

        self.assertNotEqual(len(json_obj), 0)

    def test_reload(self):
        self.strg.reload()
        self.assertNotEqual(len(self.strg.all()), 0)

        os.remove('file.json')

