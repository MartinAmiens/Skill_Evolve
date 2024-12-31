'''Définit les classes comme Competence et Jeu.
Gère la logique métier du jeu, comme les évolutions et la progression.'''

import json


class skill:
    def __init__(self, name, description, stats):
        self.name = name
        self.level = 1
        self.description = description
        self.stats = stats
        self.effects = []

    def __str__(self):
        return f"{self.name} : {self.description}\n {self.stats}\n {self.effects}"

    def level_up(self):
        """Augmente le niveau de la compétence."""
        self.level += 1

    def evolve(self):
        pass


class jeu:
    def __init__(self):
        pass
