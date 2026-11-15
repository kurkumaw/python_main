import pygame
import random

pygame.init()

# Чертеж падающего шарика
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(20, 560), 0, 25, 25)
        self.speed = 5

    def move(self):
        self.rect.y += self.speed
        # Если шарик упал за нижний край — возвращаем его наверх
        if self.rect.y > 450:
            self.reset()

    def reset(self):
        self.rect.x = random.randint(20, 560)
        self.rect.y = 0

    def draw(self, screen):
        pygame.draw.ellipse(screen, pygame.Color("gold"), self.rect)

# Главный класс самой игры
class CatchGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 450))
        pygame.display.set_caption("Поймай шарик")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = pygame.Rect(250, 400, 100, 20)
        self.ball = Ball()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Управление платформой стрелками влево и вправо
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player.x > 0:
                self.player.x -= 8
            if keys[pygame.K_RIGHT] and self.player.x < 500:
                self.player.x += 8

            self.ball.move()
            # Проверяем, поймала ли платформа шарик
            if self.player.colliderect(self.ball.rect):
                self.ball.reset()

            self.screen.fill(pygame.Color("midnightblue"))
            pygame.draw.rect(self.screen, pygame.Color("white"), self.player)
            self.ball.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

CatchGame().run()
