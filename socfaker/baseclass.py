import uuid
import random


class BaseClass(object):

    random = random

    def __init__(self):
        self.uuid = uuid

    def __str__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random') and not item.startswith('uuid'):
                if isinstance(getattr(type(self), item), property):
                    return_dict[item] = getattr(self, item)
        return str(return_dict)
    
    def to_dict(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random') and not item.startswith('uuid'):
                if isinstance(getattr(type(self), item), property):
                    return_dict[item] = getattr(self, item)
        return return_dict
    
    def __repr__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random'):
                return_dict[item] = getattr(self, item)
        return str(return_dict)

    def __iter__(self):
        return_dict = {}
        for item in dir(self):
            if not item.startswith('_') and item not in self.__dict__ and not item.startswith('random'):
                return_dict[item] = getattr(self, item)
        return iter(return_dict.items())

    def _get_data(self, file_path):
        return_list = []
        with open(file_path, "r") as filehandle:
            for item in filehandle.readlines():
                return_list.append(item)
        return return_list
