#!/usr/bin/python3
"""City"""

from models.base_model import BaseModel
import json


class City(BaseModel):
    """child from BaseModel class"""

    state_id = ""
    name = ""
