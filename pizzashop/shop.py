# Print Python module search path
import sys
from pprint import pprint
pprint(sys.path)

import pizzapy.menu
print(pizzapy.menu.MENU)
