import pygame

pygame.init()

window = pygame.display.set_mode((400,400))


window.fill((160,160,255))


GREEN = (0,180,0)

pygame.draw.circle(window, GREEN (300,300), 50)

pygame.draw.circle(window, GREEN (100,100), 50, 3)

pygame.draw.rect(window,(100,59,79),(150,150,100,100))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.Quit()