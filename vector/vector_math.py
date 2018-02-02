from __future__ import division
from vector import Vector


def add(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return Vector(map(lambda x, y: x + y, v1.getPoints(), v2.getPoints()))


def negativeVector(v):
    if isinstance(v, Vector):
        return Vector(map(lambda x: -x, v.getPoints()))


def subtract(v1, v2):
    return add(v1, negativeVector(v2))


def multiply(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return Vector(map(lambda x, y: x * y, v1.getPoints(), v2.getPoints()))


def divide(v1, v2, divider):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return Vector(map(lambda x: x / divider, add(v1, v2).getPoints()))

