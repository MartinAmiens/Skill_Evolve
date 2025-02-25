from game_logic import Game

print("Starting test...")  # Vérifie que le script se lance bien

def test_importation_game():
    try:
        game = Game()
        print("Game imported successfully!")
    except Exception as e:
        print(f"Error importing Game: {e}")
        
test_importation_game()

def test_victory():
    game = Game()
    print(game.actual_skill)  # <-- Vérifie si c'est bien un objet Skill
    assert game.actual_skill is not None, "Error: actual_skill is None"
    
    game.actual_skill.level = 99  # S'assure que le niveau peut être modifié
    assert game.actual_skill.level == 99, "Error: Level assignment failed"
    
    print("Test passed!")