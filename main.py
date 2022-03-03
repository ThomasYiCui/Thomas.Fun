import pygame

pygame.init()

screen = pygame.display.set_mode([600, 600])

class player():
    def __init__(self):
        self.x = 0
        self.y = 0
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 20, 20))

p = player()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill((255, 0, 0))
    p.draw()
    pygame.display.update()
pygame.quit()
