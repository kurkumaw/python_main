import pygame
import random

pygame.init()

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(20, 560), 0, 25, 25)
        self.speed = 5

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > 450:
            self.reset()

    def reset(self):
        self.rect.x = random.randint(20, 560)
        self.rect.y = 0

    def draw(self, screen):
        pygame.draw.ellipse(screen, pygame.Color("gold"), self.rect)

class CatchGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 450))
        pygame.display.set_caption("Поймай шарик")
        self.clock = pygame.time.Clock()
        self.running = True
        self.platform = pygame.Rect(250, 400, 100, 20)
        self.ball = Ball()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.platform.x > 0:
                self.platform.x -= 8
            if keys[pygame.K_RIGHT] and self.platform.x < 500:
                self.platform.x += 8

            self.ball.move()
            
            if self.platform.colliderect(self.ball.rect):
                self.ball.reset()

            self.screen.fill(pygame.Color("midnightblue"))
            pygame.draw.rect(self.screen, pygame.Color("white"), self.platform)
            self.ball.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

CatchGame().run()
