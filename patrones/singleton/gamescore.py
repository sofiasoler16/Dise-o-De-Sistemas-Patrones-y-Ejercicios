
class GameScore:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.score = 0
        return cls.instance

    def add_points(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def __str__(self):
        return f"Score actual: {self.score}"