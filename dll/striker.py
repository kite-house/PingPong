import pygame
from settings import font, HEIGHT, screen




class Striker:
    '''Макет игрока'''
    # Исходное положение, размеры, скорость. цвета
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
    
        self.playerRect = pygame.Rect(posx, posy, width, height)
        self.player = pygame.draw.rect(screen, self.color, self.playerRect)
 
    # Отображение обьектов
    def display(self):
        self.player = pygame.draw.rect(screen, self.color, self.playerRect)
 
    def update(self, yFac):
        self.posy = self.posy + self.speed*yFac
 
        # Ограничение
        if self.posy <= 0:
            self.posy = 0

        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT-self.height
 
        # обновление 
        self.playerRect = (self.posx, self.posy, self.width, self.height)
 
    def displayScore(self, text, score, x, y, color):
        text = font.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.playerRect