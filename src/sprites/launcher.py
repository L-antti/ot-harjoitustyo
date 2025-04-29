class Launcher:
    """Represents the bean launcher that controls shooting angles."""
    MIN_ANGLE = 10
    MAX_ANGLE = 170

    def __init__(self, position):
        """Initializes the launcher with its starting position and angle."""
        self.position = position
        self.angle = 90
        self.color = (200, 200, 200)

    def rotate(self, delta):
        """Rotates the launcher within its allowed angle range."""
        self.angle += delta
        self.angle = max(self.MIN_ANGLE, min(self.MAX_ANGLE, self.angle))
