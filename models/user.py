#!/usr/bin/python3
"""
    A class that inherits from User
    class user with this attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
from models.base_model import BaseModel
import models


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
