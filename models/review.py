#!/usr/bin/python3
"""Write a class review that inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes the Review class"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
