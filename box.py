# Created by MysteryBlokHed in 2019.
class Box:
    def __init__(self, number, value):
        if type(number) is int:
            self._number = number
        if type(value) is int or type(value) is float:
            self._value = value
        
        self._opened = False

    def get_number(self):
        return self._number
    
    def get_value(self):
        return self._value

    def set_number(self, number):
        if type(number) is int:
            self._number = number
    
    def set_value(self, value):
        if type(value) is int or type(value) is float:
            self._value = value