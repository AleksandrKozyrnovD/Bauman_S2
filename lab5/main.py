from classes import *
from animationclasses import *

def find_distance(point1, point2):
    return sqrt((point1[0]**2 - point2[0]**2) + (point1[1]**2 - point2[1]**2))

def add_red(color, increment):
    color = list(color)
    if increment < color[0] < 256 - increment:
        color[0] += increment
    if increment < color[1] < 255 - increment:
        color[1] -= increment
    if increment < color[2] < 255 - increment:
        color[2] -= increment
    return tuple(color)

def add_green(color, increment):
    color = list(color)
    if increment < color[0] < 256 - increment:
        color[0] -= increment
    if increment < color[1] < 255 - increment:
        color[1] += increment
    if increment < color[2] < 255 - increment:
        color[2] -= increment
    return tuple(color)

def add_blue(color, increment):
    color = list(color)
    if increment < color[0] < 256 - increment:
        color[0] -= increment
    if increment < color[1] < 255 - increment:
        color[1] -= increment
    if increment < color[2] < 255 - increment:
        color[2] += increment
    return tuple(color)

def orbit():
    for planet in celestials[1:]:
        planet.rotate(planet.spin, planet.center)
        planet.rotate(((find_distance(planet.center, CENTER) + 1)) / (pi * 180), CENTER)
        planet.update()
    sun.rotate(sun.spin, sun.center)

pygame.init()

#starting
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Laba 5')
clock = pygame.time.Clock()
#################

#kartinki
CENTER = (WIDTH / 2, HEIGHT / 2)
sun = Planet(display, 50, CENTER, CENTER, pi/120, yellow)
earth = Planet(display, 10, (CENTER[0] + 150, CENTER[1]), CENTER, pi/360, blue)
mars = Planet(display, 10, (CENTER[0] + 250, CENTER[1]), CENTER, pi/240, red)
celestials = [sun, earth, mars]

max_iterations = 3000
current_iteration = 0

#osnova
running = True

while running:
    #fps
    clock.tick(FPS)
    #obrabotka sobytiy
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    
    #obnovlenie kartinok/render
    display.fill(black)

    orbit()
    sun.recolor(add_red(sun.color, 0.1))
    # sun.scale(1.01, sun.center)
    sun.update()

    pygame.display.flip()
    # pygame.display.update()

pygame.quit()