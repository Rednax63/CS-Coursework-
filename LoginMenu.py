import pygame
import pygame_gui

class LoginScreen: 
    def __init__(self, window, manager):
        self.window = window 
        self.manager = manager  #creates ui manager
        self.WIDTH, self.HEIGHT = window.get_size()

        #creates back button
        backbutton_rect = pygame.Rect(0,0,150,45)
        self.backbutton = pygame_gui.elements.UIButton(
            relative_rect = backbutton_rect, 
            text = 'Back',
            manager = self.manager,
        )

        #creates submit button
        submitbutton_rect = pygame.Rect(0,40,150,45)
        self.submitbutton = pygame_gui.elements.UIButton(
            relative_rect = submitbutton_rect, 
            text = 'Submit',
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery': 'centery'}
        )
        #username input box
        userinput_rect = pygame.Rect(0,-70,300,40)
        self.userinput = pygame_gui.elements.UITextEntryLine(
            relative_rect = userinput_rect,
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.userinput.set_text("Username")
        #password input box
        passwordinput_rect = pygame.Rect(0,-20,300,40)
        self.passwordinput = pygame_gui.elements.UITextEntryLine(
            relative_rect = passwordinput_rect,
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.passwordinput.set_text_hidden(True) #hides the password
        self.passwordinput.set_text("Password")

    def handle_event(self, event): #handles inputs, events 
        self.manager.process_events(event)
        #handles window resizing
        if event.type == pygame.VIDEORESIZE: 
            self.WIDTH, self.HEIGHT = event.w, event.h
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
            self.manager.set_window_resolution((self.WIDTH, self.HEIGHT))

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.submitbutton: 
                username = self.userinput.get_text()
                password = self.passwordinput.get_text()
                print(f"Username: {username}")
                print(f"Password: {password}")
                #opens window if username and password correct
                #return "title"
            elif event.ui_element == self.backbutton:
                return "title"

        return None 
    
    def update(self, time_delta):
        self.manager.update(time_delta) #updates gui
    
    def draw(self, window):
        window.fill((99, 150, 47)) 
        self.manager.draw_ui(window) # draws gui elements


