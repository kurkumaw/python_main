import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Мой домик")

class House:
    def __init__(self):
        self.colors = ["coral", "green", "red", "blue", "plum"]
        self.wall_color = pygame.Color("coral")
        self.light_on = False
        self.wall_rect = pygame.Rect(200, 180, 200, 160)

    def change_color(self):
        new_color = random.choice(self.colors)
        self.wall_color = pygame.Color(new_color)

    def draw(self):
        
        pygame.draw.rect(screen, self.wall_color, self.wall_rect)
        pygame.draw.polygon(screen, pygame.Color("brown"), [(180, 180), (300, 90), (420, 180)])
     
        if self.light_on:
            window_color = pygame.Color("yellow")
        else:
            window_color = pygame.Color("black")
        pygame.draw.rect(screen, window_color, (275, 230, 50, 50))

house = House()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if house.wall_rect.collidepoint(event.pos):
                house.change_color()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                house.light_on = not house.light_on

    screen.fill(pygame.Color("skyblue"))
    house.draw()
    pygame.display.flip()

pygame.quit()
