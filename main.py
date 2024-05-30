# Devina Kachorin et Julieta María Fonseca Nava
# 15 avril 2024
# TP5 - Roche, Papier, Ciseaux

import random
import arcade
import arcade.gui
from attack_animation import AttackType, AttackAnimation
from game_state import GameState

# La configuration de l'écran.
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
# La hauteur de ligne par défaut pour le texte.
DEFAULT_LINE_HEIGHT = 45

# La position des images des joueurs.
PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
ATTACK_FRAME_WIDTH = 154 / 2
ATTACK_FRAME_HEIGHT = 154 / 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # La couleur de fond
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        # Initialiser les variables du jeu.
        self.player = None
        self.computer = None
        self.players = None
        self.rock = None
        self.paper = None
        self.scissors = None
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = None
        self.draw_round = None
        self.game_state = None
        self.pc_attack = None


    def setup(self, PLAYER_IMAGE_X, PLAYER_IMAGE_Y, COMPUTER_IMAGE_X, COMPUTER_IMAGE_Y):
        # Initialiser des sprites et des scores et attribuer une valeur à tous les attributs.
        self.player = None
        self.computer = None
        self.players = None
        self.rock = None
        self.paper = None
        self.scissors = None
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = {}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = None
        self.draw_round = None
        self.game_state = GameState.NOT_STARTED
        self.pc_attack = None
        self.players = arcade.SpriteList()

        # Ajouter et positionner le joueur (player).
        self.player = arcade.Sprite("assets/images/faceBeard.png", 0.22)
        self.player.center_x = PLAYER_IMAGE_X
        self.player.center_y = PLAYER_IMAGE_Y
        self.players.append(self.player)

        # Ajouter et positionner l'ordinateur.
        self.computer = arcade.Sprite("assets/images/compy.png")
        self.computer.center_x = COMPUTER_IMAGE_X
        self.computer.center_y = COMPUTER_IMAGE_Y
        self.players.append(self.computer)

        # Ajouter et positionner les attaques (roche).
        self.rock = arcade.Sprite('assets/images/srock.png', 0.5)
        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.center_x = PLAYER_IMAGE_X - 100
        self.rock.center_y = PLAYER_IMAGE_Y - 90
        self.players.append(self.rock)

        # Ajouter et positionner les attaques (papier).
        self.paper = arcade.Sprite('assets/images/spaper.png', 0.5)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.center_x = PLAYER_IMAGE_X
        self.paper.center_y = PLAYER_IMAGE_Y - 90
        self.players.append(self.paper)

        # Ajouter et positionner les attaques (ciseaux).
        self.scissors = arcade.Sprite('assets/images/scissors.png', 0.5)
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors.center_x = PLAYER_IMAGE_X + 100
        self.scissors.center_y = PLAYER_IMAGE_Y - 90
        self.players.append(self.scissors)


    def validate_victory(self):
    # Cette commande permet de déterminer qui obtient la victoire (ou s'il y a égalité).
        # Si l'ordinateur effectue la même attaque que le joueur, il y a une égalité et le score ne change pas.
        if self.computer_attack_type == self.player_attack_type:
            self.computer_score += 0
            self.player_score += 0
            self.player_won_round = None

        # Si le joueur choisit d'attaquer avec une roche et que l'ordinteur choisit d'attaquer avec un ciseau, le joueur gagne un point.
        elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
            self.player_score += 1
            self.player_won_round = True

        # Si le joueur choisit d'attaquer avec un papier et que l'ordinteur choisit d'attaquer avec une roche, le joueur gagne un point.
        elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
            self.player_score += 1
            self.player_won_round = True

        # Si le joueur choisit d'attaquer avec un ciseau et que l'ordinteur choisit d'attaquer avec un papier, le joueur gagne un point.
        elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
            self.player_score += 1
            self.player_won_round = True

        # Si aucune de ces situations se déroule, cela veu dire que l'ordinateur a gagné un point.
        else:
            self.computer_score += 1
            self.player_won_round = False

        self.game_state = GameState.ROUND_DONE



    def draw_possible_attack(self):
    # Cette commande permet de dessiner toutes les possibilités d'attaque du joueur.
        if self.player_attack_chosen != True:
            self.players.draw()

        else:
            if self.player_attack_type == AttackType.ROCK:
                self.rock.draw()
                self.rock.on_update()

            if self.player_attack_type == AttackType.PAPER:
                self.paper.draw()
                self.paper.on_update()

            if self.player_attack_type == AttackType.SCISSORS:
                self.scissors.draw()
                self.scissors.on_update()

    def draw_computer_attack(self):
    # Cette commande permet de dessiner les possibilités d'attaque de l'ordinateur.

        if self.computer_attack_type == AttackType.ROCK:
            self.rock.center_x = COMPUTER_IMAGE_X
            self.rock.draw()
            self.rock.on_update()
            self.rock.center_x = PLAYER_IMAGE_X - 100

        if self.computer_attack_type == AttackType.PAPER:
            self.paper.center_x = COMPUTER_IMAGE_X
            self.paper.draw()
            self.paper.on_update()
            self.paper.center_x = PLAYER_IMAGE_X

        if self.computer_attack_type == AttackType.SCISSORS:
            self.scissors.center_x = COMPUTER_IMAGE_X
            self.scissors.draw()
            self.scissors.on_update()
            self.scissors.center_x = PLAYER_IMAGE_X + 100

    def draw_scores(self):
    # Cette commande permet de montrer les scores du joueur et de l'ordinateur.
        arcade.draw_text(f"Le pointage du joueur est {self.player_score}", 150, 75, arcade.color.DARK_SKY_BLUE, 20, font_name = "Kenney Pixel")
        arcade.draw_text(f"Le pointage de l'ordinateur est {self.computer_score}", 640, 75, arcade.color.DARK_SKY_BLUE,20, font_name = "Kenney Pixel")

    def draw_instructions(self):
    # Cette commande permet d'afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image).
        # Lorsque le jeu commence, l'instruction suivante s'affiche.
        if self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Appuyer sur une image pour faire une attaque!", 0, 450, arcade.color.DARK_SKY_BLUE, 45, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")

        # Lorsque la ronde termine, l'instruction suivante s'affiche.
        if self.game_state == GameState.ROUND_DONE:
            arcade.draw_text("Appuyer sur 'ESPACE' pour commencer une nouvelle ronde!", 0, 450, arcade.color.DARK_SKY_BLUE, 45, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            # Lorsque le joueur gagne la ronde, l'instruction suivante s'affiche.
            if self.player_won_round == True:
                arcade.draw_text("Vous avez gagné la ronde!", 0, 350, arcade.color.DARK_SKY_BLUE, 35, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            # Lorsque l'ordinateur gagne la ronde, l'instruction suivante s'affiche.
            elif self.player_won_round == False:
                arcade.draw_text("L'ordinateur a gagné la ronde!", 0, 350, arcade.color.DARK_SKY_BLUE, 35, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            # Lorsqu'il y a une égalité, l'instruction suivante s'affiche.
            else:
                arcade.draw_text("Égalité!", 0, 350, arcade.color.DARK_SKY_BLUE, 35, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")

        # Lorsque la partie est terminée, l'instruction suivante s'affiche.
        if self.game_state == GameState.GAME_OVER:
            # Si le score du joueur est plus grand que celui de l'ordinateur, l'instruction suivante s'affiche.
            if self.computer_score < self.player_score:
                arcade.draw_text("Vous avez gagné la partie!", 0, 450, arcade.color.DARK_SKY_BLUE, 45, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            # Si le score de l'ordinateur est plus grand que celui du joueur, l'instruction suivante s'affiche.
            if self.computer_score > self.player_score:
                arcade.draw_text("L'ordinateur a gagné la partie!", 0, 450, arcade.color.DARK_SKY_BLUE, 45, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            arcade.draw_text("La partie est terminée.", 0, 390, arcade.color.DARK_SKY_BLUE, 45, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")
            arcade.draw_text("Appuyer sur 'ESPACE' pour débuter une nouvelle partie", 0, 320, arcade.color.DARK_SKY_BLUE, 35, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")


    def on_draw(self):
    # Cette commande permet d'effacer l'écran avant de dessiner.
        # Elle va dessiner l'arrière plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()

        # Afficher le titre
        arcade.draw_text(SCREEN_TITLE,0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2, arcade.color.BLACK_BEAN,80, width = SCREEN_WIDTH, align = "center", font_name = "Kenney Pixel")

        # Dessiner les instructions et un carré rouge comme contour pour chaque image
        self.draw_instructions()
        arcade.draw_rectangle_outline(PLAYER_IMAGE_X - 100, PLAYER_IMAGE_Y - 90, 70, 70, arcade.color.BOSTON_UNIVERSITY_RED, 1)
        arcade.draw_rectangle_outline(PLAYER_IMAGE_X, PLAYER_IMAGE_Y - 90, 70, 70, arcade.color.BOSTON_UNIVERSITY_RED,1)
        arcade.draw_rectangle_outline(PLAYER_IMAGE_X + 100, PLAYER_IMAGE_Y - 90, 70, 70, arcade.color.BOSTON_UNIVERSITY_RED, 1)
        arcade.draw_rectangle_outline(COMPUTER_IMAGE_X, PLAYER_IMAGE_Y - 90, 70, 70, arcade.color.BOSTON_UNIVERSITY_RED,1)
        self.draw_possible_attack()
        self.draw_computer_attack()
        self.draw_scores()


    def on_update(self, delta_time):
    # Cette commande contient toute la logique pour déplacer les objets du jeu et de simuler sa logique.
        # Vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques.
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack_chosen == True:
            # Générer une attaque de l'ordinteur en raison du choix du joueur d'attaquer.
            self.pc_attack = random.randint(0, 2)
            if self.pc_attack == 0:
                self.computer_attack_type = AttackType.ROCK
            elif self.pc_attack == 1:
                self.computer_attack_type = AttackType.PAPER
            else:
                self.computer_attack_type = AttackType.SCISSORS
            # Valider la victoire de l'ordinateur.
            self.validate_victory()

        # Changer l'état de jeu (GAME_OVER) lorsque la partie est terminée.
        if self.computer_score == 3 or self.player_score == 3:
            self.game_state = GameState.GAME_OVER


    def on_key_press(self, key, key_modifiers):
    # Cette commande est invoquée à chaque fois que l'usager tape une touche sur le clavier.

        if self.game_state == GameState.NOT_STARTED:
            # Lorsque l'usager tape sur la touche 'espace' du clavier, le jeu commence.
            if key == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE

        if self.game_state == GameState.GAME_OVER:
            # Lorsque l'usager tape sur la touche 'espace' du clavier, le jeu recommence.
            if key == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
                # Les images se repostitionnent.
                self.setup(PLAYER_IMAGE_X, PLAYER_IMAGE_Y, COMPUTER_IMAGE_X, COMPUTER_IMAGE_Y)

        if self.game_state == GameState.ROUND_DONE:
            # Lorsque l'usager tape sur la touche 'espace' du clavier, le jeu commence.
            if key == arcade.key.SPACE:
                self.game_state = GameState.ROUND_ACTIVE
                self.reset_round()


    def reset_round(self):
    # Cette commande permet de réinitialiser les variables qui ont été modifiées.
        self.computer_attack_type = -1
        self.player_attack_chosen = False
        self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
        self.player_won_round = False
        self.draw_round = False

    def on_mouse_press(self, x, y, button, key_modifiers):
    # Cette commande est invoquée lorsque l'usager clique un bouton de la souris.

        if self.game_state == GameState.ROUND_ACTIVE:

            # Lorsque l'usager clique sur l'image de la roche, l'attaque de la roche est choisie.
            if self.rock.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.player_attack_chosen = True

            # Lorsque l'usager clique sur l'image du papier, l'attaque du papier est choisie.
            if self.paper.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.player_attack_chosen = True

            # Lorsque l'usager clique sur l'image du ciseau, l'attaque du ciseau est choisie.
            if self.scissors.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.player_attack_chosen = True


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup(PLAYER_IMAGE_X, PLAYER_IMAGE_Y, COMPUTER_IMAGE_X, COMPUTER_IMAGE_Y)
    arcade.run()

if __name__ == "__main__":
    main()
