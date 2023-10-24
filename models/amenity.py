#!/usr/bin/python3
"""Write a class amenity that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity class"""
        super().__init__(*args, **kwargs)
        self.name = ""
