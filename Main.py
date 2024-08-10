import pygame
import sys
from Body import Body

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
NUM_BOIDS = 100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Boids Simulation")

clock = pygame.time.Clock()

running = True

boids = [Body(SCREEN_WIDTH, SCREEN_HEIGHT) for _ in range(NUM_BOIDS)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for boid in boids:
        boid.update(boids)
        boid.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
