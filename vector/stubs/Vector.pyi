class Vector:
    points: dict = (0,0,0)
    def __init__(self, points: dict):
        self.points = points


    def getPoints(self) -> dict:
        return self.points
