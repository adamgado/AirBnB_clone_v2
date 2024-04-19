#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            c_list = []
            for c in list(models.storage.all(C).values()):
                if c.state_id == self.id:
                    c_list.append(c)
            return c_list
