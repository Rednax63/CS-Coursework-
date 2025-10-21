import pygame
import pygame_gui
import sys

pygame.init()

#setup window
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sign Up Window")

manager = pygame_gui.UIManager((WIDTH,HEIGHT)) #creates ui manager

#creates submit button
button_rect = pygame.Rect(0,70,150,45)
button = pygame_gui.elements.UIButton(
    relative_rect = button_rect, 
    text = 'Submit',
    manager = manager,
    anchors={'centerx': 'centerx', 'centery': 'centery'}
)
#username input box
userinput_rect = pygame.Rect(0,-120,300,40)
userinput = pygame_gui.elements.UITextEntryLine(
    relative_rect = userinput_rect,
    manager = manager,
    anchors={'centerx': 'centerx', 'centery' : 'centery'}
)
userinput.set_text("Username")
#password input box
passwordinput_rect = pygame.Rect(0,-60,300,40)
passwordinput = pygame_gui.elements.UITextEntryLine(
    relative_rect = passwordinput_rect,
    manager = manager,
    anchors={'centerx': 'centerx', 'centery' : 'centery'}
)
passwordinput.set_text("Password")

#checkpassword input box
checkpasswordinput_rect = pygame.Rect(0,0,300,40)
checkpasswordinput = pygame_gui.elements.UITextEntryLine(
    relative_rect = checkpasswordinput_rect,
    manager = manager,
    anchors={'centerx': 'centerx', 'centery' : 'centery'}
)
checkpasswordinput.set_text("Re-enter Password")

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

        #tests username and password inputs by printing them out
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button: 
                username = userinput.get_text()
                password = passwordinput.get_text()
                print(f"Username: {username}")
                print(f"Password: {password}")

        manager.process_events(event)
    
    manager.update(time_delta) #updates gui 
    window.fill((99, 150, 47)) 
    manager.draw_ui(window) # draws gui elements
    pygame.display.flip()   #updates window

#quit game
pygame.quit()
sys.exit()