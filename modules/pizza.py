import math

class Pizza:
    name: str = ''
    size: int = 0
    price: float = 0

    def __init__(self, name: str, size: int, price: float) -> None:
        self.name = name
        self.size = size
        self.price = price

    def area(self) -> float:
        return math.pi * math.pow(self.size / 2, 2)

    def awesomeness(self) -> int:
        if self.name == 'Carbonara':
            return 9000

        return self.size // int(self.price) * 100

print('pizza.py module name is %s' % __name__)
if __name__ == '__main__':
    print('Carbonara is the most awesome pizza.')

