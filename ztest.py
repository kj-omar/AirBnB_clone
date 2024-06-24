#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

new = BaseModel()
print(type(new.updated_at) == datetime.datetime)
n = new.to_dict()
new = BaseModel(**n)
print(new.created_at == new.updated_at)
