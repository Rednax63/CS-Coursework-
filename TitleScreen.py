import pygame
import pygame_gui
import sys

pygame.init()

#setup window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Title Screen")

manager = pygame_gui.UIManager((WIDTH,HEIGHT)) #creates ui manager

#creates log in button
button_rect = pygame.Rect(100,150,150,45)
button = pygame_gui.elements.UIButton(
    relative_rect = button_rect, 
    text = 'Log In',
    manager = manager,
    anchors={'centerx': 'centerx', 'centery': 'centery'}
)

#creates sign up button
button_rect = pygame.Rect(-100,150,150,45)
button = pygame_gui.elements.UIButton(
    relative_rect = button_rect, 
    text = 'Sign Up',
    manager = manager,
    anchors={'centerx': 'centerx', 'centery': 'centery'}
)

clock = pygame.time.Clock()
fullscreen = False
running = True

#game loop 
while running:
    time_delta = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #handles window resizing
        elif event.type == pygame.VIDEORESIZE: 
            WIDTH, HEIGHT = event.w, event.h
            window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            manager.set_window_resolution((WIDTH, HEIGHT))

        manager.process_events(event)
    
    manager.update(time_delta) #updates gui 
    window.fill((99, 150, 47)) 
    manager.draw_ui(window) # draws gui elements
    pygame.display.flip()   #updates window

#quit game
pygame.quit()
sys.exit()