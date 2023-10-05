class calculator:
	'''
	Calculator class that emulates the four basic operations,
	Addition, Subtraction, Multiplication and Division
	between a vector and scalar object.
	...
	Attributes
	----------
	vect: list[int | float]
		Stores a list of integers or floats that represents the vector.
	...
	Methods
	-------
	__add__ : Override for the '+' operation.
	__mul__ : Override for the '*' operation.
	__sub__ : Override for the '-' operation.
	__truediv__ : Override for the '/' operation.
	'''
	def __init__(self, arr: list[int | float]) -> None:
		'''Constructor class for the calculator class'''
		try:
			for i in arr:
				if isinstance(i, (int, float)) is False:
					raise AssertionError("Init values are not valid.")
			self.vect = arr
		except Exception as e:
			print(f"{type(e).__name__}: {e}")

	def __add__(self, object) -> None:
		'''
		Override for the '+' operator
		Applies the '+' operator and prints the result
		'''
		try:
			if isinstance(object, (int, float)) is False:
				raise AssertionError("Scalar is not of a valid type.")
			for i in range(len(self.vect)):
				self.vect[i] += object
			print(self.vect)
		except Exception as e:
			print(f"{type(e).__name__}: {e}")

	def __mul__(self, object) -> None:
		'''
		Override for the '*' operator
		Applies the '*' operator and prints the result
		'''
		try:
			if isinstance(object, (int, float)) is False:
				raise AssertionError("Scalar is not of a valid type.")
			for i in range(len(self.vect)):
				self.vect[i] *= object
			print(self.vect)
		except Exception as e:
			print(f"{type(e).__name__}: {e}")

	def __sub__(self, object) -> None:
		'''
		Override for the '-' operator
		Applies the '-' operator and prints the result
		'''
		try:
			if isinstance(object, (int, float)) is False:
				raise AssertionError("Scalar is not of a valid type.")
			for i in range(len(self.vect)):
				self.vect[i] -= object
			print(self.vect)
		except Exception as e:
			print(f"{type(e).__name__}: {e}")

	def __truediv__(self, object) -> None:
		'''
		Override for the '-' operator
		Applies the '-' operator and prints the result
		'''
		try:
			if isinstance(object, (int, float)) is False:
				raise AssertionError("Scalar is not of a valid type.")
			if object == 0:
				raise ZeroDivisionError("No divide by 0.")
			for i in range(len(self.vect)):
				self.vect[i] /= object
			print(self.vect)
		except Exception as e:
			print(f"{type(e).__name__}: {e}")