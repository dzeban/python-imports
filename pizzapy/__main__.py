# pizzapy/__main__.py
# this module allows to run the package with `python3 -m pizzapy`

from pizzapy.menu import MENU

print('Awesomeness of pizzas:')
for pizza in MENU:
    print(pizza.name, pizza.awesomeness())
