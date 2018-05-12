from __future__ import print_function


class Vector:
    points = [0, 0, 0]

    def __init__(self, points):
        if isinstance(points, list) and len(points) == 3:
            self.points = points
        else:
            print("The points for the vector must be a list with length 3")

    def getPoints(self):
        return self.points
