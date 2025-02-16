"""Définit les classes comme Competence et Jeu.
Gère la logique métier du jeu, comme les évolutions et la progression."""

import json


class Skill:
    def __init__(self, name, description, stats):
        self.name = name
        self.level = 1
        self.description = description
        self.stats = stats
        self.effects = []

    def __str__(self):
        return f"{self.name}: {self.description}\n{self.stats}\n{self.effects}"

    def level_up(self):
        """Augmente le niveau de la compétence."""
        self.level += 1

    def evolve(self, choix):
        """Applique une évolution en fonction du choix."""
        self.name = choix
        self.level_up()
        # Ajoute de nouveaux effets ou modifie les stats
        self.effects.append(f"Évolution vers {choix}")


class Game:
    def __init__(self):
        self.actual_skill = None
        self.timer = 30
        self.skill_tree = self.load_skill_tree()

    def load_skill_tree(self):
        """Charge l'arbre d'évolution depuis un fichier
        JSON avec gestion d'erreur."""
        try:
            with open("data/evolutions.json", "r") as fichier:
                return json.load(fichier)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erreur: Impossible de charger l'arbre des compétences.")
            return {}

    def init_base_skill(self, name, description, stats):
        self.actual_skill = Skill(name, description, stats)

    def get_evolution_choices(self):
        """Propose les choix d'évolution disponibles."""
        level = str(self.actual_skill.level)

        # Vérifie si la compétence actuelle est bien dans l'arbre
        # des compétences
        if self.actual_skill.name not in self.skill_tree:
            print(f"Aucune évolution trouvée pour {self.actual_skill.name}.")
            return []

        return self.skill_tree[self.actual_skill.name].get(level, [])

    def appliquer_choix(self, choix):
        """Applique le choix d'évolution."""
        self.actual_skill.evolve(choix)
