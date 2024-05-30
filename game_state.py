from enum import Enum

# Cette classe permet de représenter les différents états possibles du jeu.
class GameState(Enum):
    # Le jeu n'a pas encore commencé.
    NOT_STARTED = 0
    # La ronde actuelle est terminée.
    ROUND_DONE = 1
    # Le jeu est terminé.
    GAME_OVER = 2
    # La ronde est en cours.
    ROUND_ACTIVE = 3
