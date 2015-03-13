import pygame

class NPC():

    image = pygame.image.load("images/greenalien.gif")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_down(self):
        self.y +=   5


class Bullet():

    image = pygame.image.load("images/bullet.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 30


class Player():

    image = pygame.image.load("images/spaceship1.gif")

    def __init__(self):
        self.x = 250
        self.y = 300

    def move(self, left):
        if left == True:
            self.x -= 40
        else:
            self.x += 40
