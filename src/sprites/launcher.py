class Launcher:
    MIN_ANGLE = 10
    MAX_ANGLE = 170

    def __init__(self, position):
        self.position = position
        self.angle = 90
        self.color = (200, 200, 200)

    def rotate(self, delta):
        self.angle += delta
        self.angle = max(self.MIN_ANGLE, min(self.MAX_ANGLE, self.angle))
