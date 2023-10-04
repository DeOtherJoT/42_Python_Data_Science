from abc import ABC, abstractmethod

class Character(ABC):
	'''Abstract class to represent a character'''

	@abstractmethod
	def __init__(self, first_name, is_alive=True):
		'''
		Constructor for the Character class
		...
		Attributes
		----------
		first_name: str
			The first name of the character
		is_alive: bool
			The status of the character
		'''
		self.first_name = first_name
		self.is_alive = is_alive
	
	def die(self):
		'''
		Method that changes the is_alive attribute of a
		character to False
		'''
		self.is_alive = False


class Stark(Character):
	'''
	Class that inherits from the Character class
	'''
	def __init__(self, first_name, is_alive=True):
		'''
		Constructor for the Stark class
		'''
		super().__init__(first_name, is_alive)