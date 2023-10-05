from S1E9 import Character


class Baratheon(Character):
    '''Representing the Baratheon family.'''
    def __init__(self, first_name, is_alive=True):
        '''
        Constructor for the Baratheon class.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        '''Returns a user-readable string of the class attributes'''
        return (
            f"Character is {self.first_name} {self.family_name}, "
            f"with {self.eyes} eye colour and {self.hairs} hair. "
        )

    def __repr__(self) -> str:
        '''Returns a programmer-readable string for the class attributes
        The returned string will be able to reconstruct the class'''
        return (f"Baratheon{self.first_name, self.is_alive}")


class Lannister(Character):
    '''Representing the Lannister family.'''
    def __init__(self, first_name, is_alive=True):
        '''
        Constructor for the Lannister class.
        '''
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        '''Returns a user-readable string of the class attributes'''
        return (
            f"Character is {self.first_name} {self.family_name}, "
            f"with {self.eyes} eye colour and {self.hairs} hair. "
        )

    def __repr__(self) -> str:
        '''Returns a programmer-readable string for the class attributes
        The returned string will be able to reconstruct the class'''
        return (
            f"Lannister{self.first_name, self.is_alive}"
        )

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        '''Creates a Lannister object using a class method'''
        return cls(first_name, is_alive)
