class calculator:
    '''
    Calculator class that emulates the three basic operations,
    Addition, Subtraction, Dot Product
    between two vector objects.
    ...
    Methods
    -------
    dotproduct(V1, V2): Returns the dot product between two vectors
    add_vec(V1, V2): Prints the vector after adding up the two vectors
    sous_vect(V1, V2): Prints the vector after subtracting the two vectors
    '''

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Executes a dot product of the two vectors and prints the result.'''
        total = 0
        for a, b in zip(V1, V2):
            total += (a * b)
        print(f"Dot product is: {total}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Executes a sum between two vectors and prints the result'''
        result = [a + b for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Executes a subtraction between two vectors and prints the result'''
        result = [a - b for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
