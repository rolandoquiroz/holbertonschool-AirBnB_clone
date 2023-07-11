#!/usr/bin/python3

"""

This module define a TestBaseModel Class

"""

import unittest
from time import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    A TestBaseModel Class
    """
    def setUp(self):
        self.mdl = BaseModel()
        self.start = time()

    def tearDown(self):
        self.end = time()

    def test_id(self):
        self.assertTrue(self.mdl.id)

    def test_created_at(self):
        self.assertTrue(self.mdl.created_at)

    def test_str(self):
        self.assertEqual(str(self.mdl),
                         f'[BaseModel] ({self.mdl.id}) {self.mdl.__dict__}')

    def test_save(self):
        first_time = self.mdl.updated_at
        self.mdl.save()
        second_time = self.mdl.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_to_dict(self):
        self.assertIn('__class__', self.mdl.to_dict())
