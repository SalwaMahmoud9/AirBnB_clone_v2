#!/usr/bin/python3
"""Review"""

from models.base_model import BaseModel
import json


class Review(BaseModel):
    """child from BaseModel class"""

    place_id = ""
    user_id = ""
    text = ""
