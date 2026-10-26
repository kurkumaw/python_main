import sys
import pygame

print("Напишите цвета на английском")

while True:
    user_walls = input("Введите цвет для стен: ")
    try:
        color_walls = pygame.Color(user_walls)
        break  
    except ValueError:
        print(f"Ошибка! Цвет '{user_walls}' не найден. Попробуйте еще раз.")

while True:
    user_roof = input("Введите цвет для крыши: ")
    try:
        color_roof = pygame.Color(user_roof)
        break  
    except ValueError:
        print(f"Ошибка! Цвет '{user_roof}' не найден. Попробуйте еще раз.")

print("Готово! Откройте появившееся графическое окно, чтобы увидеть результат.")

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Простая раскраска дома")

color_bg = pygame.Color("black")
color_border = pygame.Color("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, color_walls, (200, 230, 200, 200))
    pygame.draw.rect(screen, color_border, (200, 230, 200, 200), 3)

    roof_points = [(170, 230), (300, 100), (430, 230)]
    pygame.draw.polygon(screen, color_roof, roof_points)
    pygame.draw.polygon(screen, color_border, roof_points, 3)

    pygame.display.flip()