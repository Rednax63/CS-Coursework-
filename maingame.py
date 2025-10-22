import pygame 
import pygame_gui

#imports screens and menus
from TitleScreen import TitleScreen
from LoginMenu import LoginMenu 
from SignupMenu import SignupMenu 

pygame.init

#sets up window
WIDTH, HEIGHT = 800, 600 
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Untitled")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True

#default to title screen
current_screen = TitleScreen(window, manager)

while running: 
    time_delta = clock.tick(60) / 1000
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        elif event.type == pygame.VIDEORESIZE: 
            WIDTH, HEIGHT = event.w, event.h 
            window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            manager.set_window_resolution((WIDTH, HEIGHT))
            current_screen.on_resize(WIDTH, HEIGHT)

        #current screen handles all events 
        next_screen = current_screen.handle_event(event)
        #switches screens
        if next_screen: 
            current_screen = next_screen
    
    current_screen.update(time_delta)
    window.fill((99, 150, 47))
    current_screen.draw(window)
    pygame.display.flip()

pygame.quit()


