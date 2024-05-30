import arcade
import random
from enum import Enum

# Cette classe permet de définir un type énuméré pour les différents types d'attaques.
class AttackType(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

# Cette classe permet de gérer les animations des attaques.
class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    # Vitesse de l'animation (nombre de changements de texture par seconde).
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        super().__init__()
        # Définir le type d'attaque (ROCHE, PAPIER, ou CISEAU).
        self.attack_type = attack_type
        
        # Choisir les images pour l'attaque.
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/images/srock.png"), # Image roche 'normale'.
                arcade.load_texture("assets/images/srock-attack.png"), # Image roche 'en attaque'.
            ]
        #     
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/images/spaper.png"), # Image papier 'normale'.
                arcade.load_texture("assets/images/spaper-attack.png"), # Image papier 'en attaque'.
            ]
        #    
        else:
            self.textures = [
            arcade.load_texture("assets/images/scissors.png"), # Image ciseau 'normale'.
            arcade.load_texture("assets/images/scissors-close.png"), # Image ciseau 'en attaque'.
            ]

        # Application de l'échelle aux sprites (ajuster la taille des images).
        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)
        # Temps entre chaque changement d'image.
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

    def on_update(self, delta_time: float = 1 / 60):
    # Mettre à jour l'animation en fonction du temps écoulé.
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0
