import pygame

pygame.init()
font = pygame.font.Font('meta/mont.ttf', 25)
 
# RGB настройка цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0 ,255)
GREEN = (50, 205, 50)

# Параметры экрана и название окна
WIDTH, HEIGHT = 1634, 907
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")
 
clock = pygame.time.Clock()   
FPS = 60 # скорость игры 
 