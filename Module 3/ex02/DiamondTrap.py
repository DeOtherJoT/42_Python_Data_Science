from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''Representing the King class'''

    def __init__(self, first_name, is_alive=True):
        '''Class constructor for the King class'''
        super().__init__(first_name, is_alive)

    def set_eyes(self, color: str):
        '''Sets the eye colour of the King character'''
        if (isinstance(color, str)):
            self.eyes = color
        else:
            print("The King does not accept the eye colour.")

    def set_hairs(self, color: str):
        '''Sets the hair colour of the King character'''
        if (isinstance(color, str)):
            self.hairs = color
        else:
            print("The King does not accept the eye colour.")

    def get_eyes(self):
        '''Getter function for the eye colour of the King.'''
        return (self.eyes)

    def get_hairs(self):
        '''Getter function for the hair colour of the King.'''
        return (self.hairs)

    def __repr__(self) -> str:
        return (f"{type(self).__name__}{self.first_name, self.is_alive}")
