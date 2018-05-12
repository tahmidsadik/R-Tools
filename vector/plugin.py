import sys

sys.path.append("C:\\Users\\tahmi\\PycharmProjects\\R-Tools\\Vector\\")
from vector import Vector
from vmath import add, subtract, multiply, divide

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(add(v1, v2).getPoints())
print(subtract(v1, v2).getPoints())
print(multiply(v1, v2, 2).getPoints())
print(divide(v1, v2, 2).getPoints())
