import pygame
class Background:
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/bg.png')
        self.position = 0
        self.uncoloredSprite = pygame.image.load('data/gfx/bg.png') 
    def setSprite(self, tint):  
        copy = self.uncoloredSprite.copy()
        self.sprite = copy
