#!/usr/bin/python3

"""

This module define a TestBaseModel Class

"""

import unittest
import os
import json
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """
    A TestBaseModel Class
    """

    def test_string_representation(self):
        my_model = BaseModel()
        self.assertEqual(str(my_model),
                         f'[BaseModel] ({my_model.id}) {my_model.__dict__}')
