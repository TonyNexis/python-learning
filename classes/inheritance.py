from dataclasses import dataclass
from typing import ClassVar


class Store:
    apple = 22
    water = 100

    def __init__(self, name):
        self.name = name

    # @classmethod
    def info(self):
        return (f' >> {self.name} has apple = {self.apple} and water = {self.water}')
    
silpo = Store('Silpo')

print(silpo.info())

@dataclass
class NewStore:
    name: str
    apple: ClassVar[int] = 41
    water: ClassVar[int] = 99

    def info(self):
        return f' >> {self.name} has {self.apple} apples and {self.water} water.'
    
atb = NewStore('ATB')

print(atb.info())
