#!/usr/bin/python3
"""Write a class review that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
