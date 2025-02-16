'''Gère l’affichage graphique, les boutons et les événements utilisateur.'''

import tkinter as tk
from game_logic import Game

class GameGUI:
    def __init__(self, root):
        self.game = Game()
        self.game.init_base_skill("Sleeping",
                    "Permet de récupérer de l'énergie.",
                    stats={"récupération": 10, "durée": 8}
                    )

        self.root = root
        self.root.title("Skill_evolve_game")

        # Label pour afficher la compétence actuelle
        self.skill_label = tk.Label(root, text=self.get_skill_text(), font=("Arial", 14))
        self.skill_label.pack(pady=10)

        # Bouton pour proposer des évolutions
        self.evolution_button = tk.Button(root, text="Évoluer", command=self.show_evolutions)
        self.evolution_button.pack()

        # Frame pour afficher les choix d'évolution
        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack()



    def get_skill_text(self):
        return f"Compétence actuelle: {self.game.actual_skill.name} (Niveau {self.game.actual_skill.level})"


    def show_evolutions(self):
        # Efface les anciens boutons
        for widget in self.choices_frame.winfo_children():
            widget.destroy()
        
        choices = self.game.get_evolution_choices()
        
        if not choices:
            tk.Label(self.choices_frame, text="Aucune évolution disponible.").pack()
            return
        
        for choice in choices:
            btn = tk.Button(self.choices_frame, text=choice, command=lambda c=choice: self.apply_evolution(c))
            btn.pack(pady=5)

    def apply_evolution(self, choix):
        """Applique l'évolution choisie et met à jour l'affichage sans afficher directement les nouvelles évolutions."""
        self.game.appliquer_choix(choix)
        self.skill_label.config(text=self.get_skill_text())

        # Effacer les boutons des anciens choix d'évolution pour éviter qu'ils restent affichés
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

def run_game():
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()

