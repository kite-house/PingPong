import pygame
from settings import BLACK, WHITE, RED, BLUE, GREEN, WIDTH, HEIGHT, screen, clock, FPS, font
from dll.striker import Striker
from dll.ball import Ball
import time
def main():
    running = True
    pause = False
 
    # Определение обьектов
    player1 = Striker(20, 0, 10, 100, 10, RED)
    player2 = Striker(WIDTH-30, 0, 10, 100, 10, BLUE)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
 
    listOfplayers = [player1, player2]
 
    # Начальные параметры игроков
    player1Score, player2Score = 0, 0
    player1YFac, player2YFac = 0, 0
 
    while running:
        bg = pygame.image.load("meta/table.jpg")
        screen.fill(BLACK)
        screen.blit(bg, (0, 0))

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

        if player1Score >= 1 or player2Score >= 15:
            pause = True
            while pause:
                if player1Score >= 15:
                    text1 = font.render('Победитель: Игрок 1!', True, GREEN)
                if player2Score >= 15:
                    text1 = font.render('Победитель: Игрок 2!', True, GREEN)
                
                # Текст
                text2 = font.render('Спасибо за игру! Автор: KITE-DEV.', True, GREEN)
                textRect1 = text1.get_rect(center = (WIDTH/2, HEIGHT/2))
                textRect2 = text2.get_rect(center = (WIDTH/2, HEIGHT/2+50))
                screen.fill(BLACK) # меняем фон
                screen.blit(text1, textRect1)
                screen.blit(text2, textRect2)

                # принимаем и обновляем игру для перезапуска
                pygame.display.flip()
                time.sleep(1)
                ball.reset()
                player1Score, player2Score = 0, 0
                player1YFac, player2YFac = 0, 0
                time.sleep(3)
                pause = False # рестарт

            

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