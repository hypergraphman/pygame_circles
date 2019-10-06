import pygame
import random

size = width, height = 400, 300
main_screen = pygame.display.set_mode(size)
circles_screen = pygame.Surface(main_screen.get_size())
background = pygame.Surface(main_screen.get_size())
clock = pygame.time.Clock()

running = True
x_pos = 0
y_pos = 400
v = 100  # пикселей в секунду
fps = 60
circle_radius = 10
circles = []
stars = [[random.randint(0, 400), random.randint(0, 300),
          (255, 255, 255), random.randint(32, 130)] for i in range(300)]


def draw_stars(scr, stars, height, fps):
    scr.fill((0, 0, 0))
    for star in stars:
        if star[1] > height:
            star[1] = - 6
            star[3] = random.randint(32, 130)
        star[1] += int(star[3] / (fps / 4))
        pygame.draw.rect(scr, star[2], (star[0], star[1], 2, 6), 0)


while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            circles.append([x, y, (r, g, b)])

    # отрисовка и изменение свойств объектов
    main_screen.fill((0, 0, 0))
    draw_stars(background, stars, height, fps)
    circles_screen.fill((0, 0, 0))
    circles_screen.blit(background, (0, 0))

    for circle in circles:
        if circle[1] < height - circle_radius:
            circle[1] += int(v / fps)
        pygame.draw.circle(circles_screen, circle[2], (circle[0], circle[1]), circle_radius)
    main_screen.blit(circles_screen, (0, 0))

    clock.tick(fps)

    # обновление экрана
    pygame.display.flip()

pygame.quit()
