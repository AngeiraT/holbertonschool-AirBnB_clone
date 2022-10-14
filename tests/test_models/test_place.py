#!/usr/bin/python3
""" Unittest for Place class """
import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

class Test_Place(unittest.TestCase):
    def setup():
        """ sets up Place tests """
        pass
