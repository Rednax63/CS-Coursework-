import pygame
import sys

pygame.init()

#set up empty window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Empty Window")

#game loop - keeps game updating until close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  #empty window
    pygame.display.flip()   #update window

#quit game
pygame.quit()
sys.exit()
