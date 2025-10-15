import module
from module import make_car
from module import make_car as mc
import module as md
from module import *

car = mc('subaru', 'outback', color='blue', tow_package=True)
print(car)