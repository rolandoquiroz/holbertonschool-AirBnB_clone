#!/usr/bin/python3

"""

This module define a TestBaseModel Class

"""

import unittest
from time import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A TestBaseModel Class
    """
    def setUp(self):
        self.bmdl = BaseModel()
        self.start = time()

    def tearDown(self):
        self.end = time()

    def test_id(self):
        self.assertTrue(self.bmdl.id)

    def test_created_at(self):
        self.assertIs(type(self.bmdl.created_at), datetime)

    def test_str(self):
        self.assertEqual(str(self.bmdl),
                         f'[BaseModel] ({self.bmdl.id}) {self.bmdl.__dict__}')

    def test_save(self):
        first_time = self.bmdl.updated_at
        self.bmdl.save()
        second_time = self.bmdl.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_to_dict(self):
        self.assertIn('__class__', self.bmdl.to_dict())
