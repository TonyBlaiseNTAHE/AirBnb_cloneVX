#!/usr/bin/python3

"""
base_model module
"""
#importing modules for date
from datetime import datetime
import uuid

# declare a class called BaseModel that define all the common attributes/methods for other classes
class BaseModel:
    """
    class baseModels: defines all the common attributes for other classes
    """
    # declaring the class constructor
    def __init__(self):
        # declaring public instance attributes
        # id -string -assing with an uuid when an instance is created.
        # by declaring id you use uuid.uuid4() to generate unique id but do not forget to string 
        self.id = str(uuid.uuid4())
        # created_at: datetime - assign with the current datetime when an instance is created
        self.created_at = datetime.now()
        # updated_at datetime - assing with the current datetime when an instance is created and it will be updated every time you change your project
        self.update_at = datetime.now()
    # declaring public instance methods:
    # __str__: represent a string representation of an object
    #         should print :[<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        s = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return s
    # save(self): updates the public instance attribute updated_at with the current datetime
    def save(self):
        """update updated_at with current datetime"""
        self.update_at = datetime.now()
    # to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
    #                by using self.__dict__, only instance attributes set will be returned 
    #                a key __class__ must be added to this dictionary with the class name of the object
    # created_at and update_at must be converted to string object in ISO format:
    # format: format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259) 
    # you can use isoformat() of datetime object
    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        dt = {}
        for key, value in self.__dict__.items():
            if key == 'updated_at' or value == 'created_at':
                dt[key] = value.isoformat()
            dt[key] = value
        dt['__class__'] = self.__class__.__name__
        return dt