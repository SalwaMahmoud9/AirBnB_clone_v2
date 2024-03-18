#!/usr/bin/python3
"""User"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """child from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
