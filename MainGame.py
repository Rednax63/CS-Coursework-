import pygame 
import pygame_gui

#imports screens and menus
from TitleScreen import TitleScreen
from LoginMenu import LoginScreen
from SignupMenu import SignupScreen

pygame.init()

#sets up window
WIDTH, HEIGHT = 800, 600 
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Untitled")

manager = manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')
clock = pygame.time.Clock()
running = True

#default to title screen
current_screen = TitleScreen(window, manager)

while running: 
    time_delta = clock.tick(60) / 1000
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        #current screen handles all events 
        next_screen = current_screen.handle_event(event)

        #switches between screens
        if next_screen == "login":
            manager.clear_and_reset()
            current_screen = LoginScreen(window, manager)

        elif next_screen == "signup":
            manager.clear_and_reset()
            current_screen = SignupScreen(window, manager)

        elif next_screen == "title":
            manager.clear_and_reset()
            current_screen = TitleScreen(window, manager)

    current_screen.update(time_delta)
    window.fill((99, 150, 47))
    current_screen.draw(window)
    pygame.display.flip()

pygame.quit()



