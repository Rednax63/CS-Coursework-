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
button_rect = pygame.Rect((WIDTH - 130, HEIGHT - 70), (100,40))
button = pygame_gui.elements.UIButton(
    relative_rect = button_rect, 
    text = 'Submit',
    manager = manager
)

clock = pygame.time.Clock()

#game loop 
running = True
while running:
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)
    
    manager.update(time_delta) #updates gui state
    window.fill((0, 0, 0))  # clears screen
    manager.draw_ui(window) # draws gui elementw
    pygame.display.flip()   #update window

#quit game
pygame.quit()
sys.exit()
