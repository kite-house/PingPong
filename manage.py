import pygame
from settings import BLACK, WHITE, RED, BLUE, GREEN, WIDTH, HEIGHT, screen, clock, FPS, font
from dll.striker import Striker
from dll.ball import Ball
def main():
    running = True
 
    # Определение обьектов
    player1 = Striker(20, 0, 10, 100, 10, RED)
    player2 = Striker(WIDTH-30, 0, 10, 100, 10, BLUE)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
 
    listOfplayers = [player1, player2]
 
    # Начальные параметры игроков
    player1Score, player2Score = 0, 0
    player1YFac, player2YFac = 0, 0
 
    while running:
        screen.fill(BLACK)
 
        # Обработчик евентов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2YFac = -1
                if event.key == pygame.K_DOWN:
                    player2YFac = 1
                if event.key == pygame.K_w:
                    player1YFac = -1
                if event.key == pygame.K_s:
                    player1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1YFac = 0
 
        # Обнаружение столкновений
        for player in listOfplayers:
            if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
                ball.hit()
 
        # Обновление обьектов
        player1.update(player1YFac)
        player2.update(player2YFac)
        point = ball.update()
 
        # распределение очков
        if point == -1:
            player1Score += 1
        elif point == 1:
            player2Score += 1

        if player1Score >= 0 or player2Score >= 15:
            clock.tick(0)
            text = font.render('GAME OVER', True, GREEN)
            textRect = text.get_rect()
            textRect.center(WIDTH, HEIGHT)
            screen.blit(text, textRect)
            running = False

        # респавн мяча
        if point:  
            ball.reset()
 
        # Отображение обьектов
        player1.display()
        player2.display()
        ball.display()
 
        # Отображение очков игроков
        player1.displayScore("Игрок1 : ", player1Score, 100, 20, WHITE)
        player2.displayScore("Игрок2 : ", player2Score, WIDTH-100, 20, WHITE)
 
        pygame.display.update()
        clock.tick(FPS)    
 
 
if __name__ == "__main__":
    main()
    pygame.quit()