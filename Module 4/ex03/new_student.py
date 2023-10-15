import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''
    Generates the id for the Student class, made up of 15 randomly generated
    lowercase alphabets.
    '''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''
    Student class that takes in the student's first name and surname, and
    optionally the student's active status.
    Constructed using the dataclass decorator, that automaticaly does the
    general __init__, __repr__, etc.
    '''
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        '''
        Special class method that executes after __init__, usually because
        it requires some values that are only "saved" after the __init__.
        '''
        self.login = self.name[0] + self.surname
