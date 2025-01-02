# Initialize the game
# Lie la logique du jeu et l’interface utilisateur.
# Contient la boucle principale.

from game_logic import jeu
# Créer une instance du jeu
jeu = jeu()

# Initialiser une compétence de départ
jeu.init_base_skill("Sleeping",
                    "Permet de récupérer de l'énergie.",
                    stats={"récupération": 10, "durée": 8}
                    )

# Proposer des évolutions
choix = jeu.proposer_evolutions()
print(f"Choix disponibles : {choix}")

# Appliquer un choix
jeu.appliquer_choix("Récupération")
print(f"Compétence après évolution : {jeu.actual_skill.name}")
