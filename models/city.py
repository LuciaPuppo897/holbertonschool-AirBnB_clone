#!/usr/bin/python3
"""Write a class city that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """class city"""
    def __init__(self, *args, **kwargs):
        """Initializes the City class"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
