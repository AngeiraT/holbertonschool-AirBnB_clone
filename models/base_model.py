#!/usr/bin/python3
"""
Class BaseModel
"""

from datetime import datetime
import uuid
import models
# dtm = dateformat
dtm = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            # Check for keys and value in the items
            for key, value in kwargs.items():
                # Assign key the actual date of creation
                if key == "created_at":
                    self.created_at = datetime.strptime(
                    value, dtm)
                # Assign key the updated date
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                    value, dtm)
                # Assign value to key
                # self: object which attribute will be assigned
                # key: attribute of the object assigned
                # value: value which will be assigned to the variable
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            # Assign aleotory id
            self.id = str(uuid.uuid4)
            # Assign updated date
            self.created_at = datetime.now()
            # Update the last date modification
            self.updated_at = self.created_at
            # If is a new instance
            # not from a dictionary representation
            models.storage.new(self)

    def __str__(self):
        """Returns the class name, id and dictionary attrbutes"""
        return "[{}] ({}) {}" .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates public instance attribute update_at with the actual date and hour"""
        self.updated_at = datetime.now()
        # Call method save(self) of storage
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all the keys / values of instance dictionary"""
        dic = {
            'id': self.id,
            'created_at': self.created_at.strftime(dtm),
            'updated_at': self.updated_at.strftime(dtm),
            '__class__': self.__class__.__name__
        }
        return dic
