from gamescore import GameScore

# Sirve para que pueda existir solo una instancia de un objeto

score1 = GameScore()

score1.add_points(10)

score1.add_points(10)

print(score1)

score2 = GameScore()

print(score2)

score2.add_points(20)

print(score2)

score1.reset_score()

print(score1)