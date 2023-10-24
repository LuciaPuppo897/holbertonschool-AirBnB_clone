#!/usr/bin/python3
"""Write a class state that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """class state"""
    def __init__(self, *args, **kwargs):
        """Initializes the state class"""
        super().__init__(*args, **kwargs)
        self.name = ""
