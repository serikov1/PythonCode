from typing import List


class Player:
    id: int
    name: str
    scores: int
    games: List[int]

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.scores = 0
        self.games = []

    def add_result(self, game_id: int, scores: int) -> None:
        self.games.append(game_id)
        self.scores += scores
        return None

    def get_mean(self) -> float:
        return self.scores / len(self.games) if self.games else 0


p = Player(1, 'Bilbo')
print(p.id)
print(p.name)
print(p.scores)
print(p.games)

p.add_result(15, 10)
p.add_result(21, 5)
print(p.scores)
print(p.games)
print(p.get_mean())