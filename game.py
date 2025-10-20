import pygame
import pygame_gui
import sys

pygame.init()

#set window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game")

manager = pygame_gui.UIManager((WIDTH,HEIGHT)) #creates ui manager

#creates submit button
button_rect = pygame.Ret((WIDTH - 130, HEIGHT - 70), (100,40))
button = pygame_gui.elements.UIButton(
    relative_rect = button_rect, 
    text = 'Submit',
    manager = manager
)

#game loop - keeps game updating until close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()   #update window

#quit game
pygame.quit()
sys.exit()
