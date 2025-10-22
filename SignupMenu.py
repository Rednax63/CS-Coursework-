import pygame
import pygame_gui

class SignupScreen: 
    def __init__(self, window, manager):
        self.window = window 
        self.manager = manager 
        self.WIDTH, self.HEIGHT = window.get_size()

        #creates back button
        backbutton_rect = pygame.Rect(0,0,150,45)
        self.backbutton = pygame_gui.elements.UIButton(
            relative_rect = backbutton_rect, 
            text = 'Back',
            manager = self.manager,
        )

        #creates submit button
        submitbutton_rect = pygame.Rect(0,70,150,45)
        self.submitbutton = pygame_gui.elements.UIButton(
            relative_rect = submitbutton_rect, 
            text = 'Submit',
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery': 'centery'}
        )
        #username input box
        userinput_rect = pygame.Rect(0,-120,300,40)
        self.userinput = pygame_gui.elements.UITextEntryLine(
            relative_rect = userinput_rect,
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.userinput.set_text("Username")
        #password input box
        passwordinput_rect = pygame.Rect(0,-60,300,40)
        self.passwordinput = pygame_gui.elements.UITextEntryLine(
            relative_rect = passwordinput_rect,
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.passwordinput.set_text("Password")

        #checkpassword input box
        checkpasswordinput_rect = pygame.Rect(0,0,300,40)
        self.checkpasswordinput = pygame_gui.elements.UITextEntryLine(
            relative_rect = checkpasswordinput_rect,
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery' : 'centery'}
        )
        self.checkpasswordinput.set_text("Re-enter Password")

    def handle_event(self, event):
        self.manager.process_events(event)
        #handles window resizing
        if event.type == pygame.VIDEORESIZE: 
            self.WIDTH, self.HEIGHT = event.w, event.h
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
            self.manager.set_window_resolution((self.WIDTH, self.HEIGHT))

        #tests username and password inputs by printing them out
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.submitbutton: 
                username = self.userinput.get_text()
                password = self.passwordinput.get_text()
                check = self.checkpasswordinput.get_text()

                if password == check:
                    print(f"Account created")
                    return "login" #loads login page
                else:
                    print(F"Passwords do not match")

            elif event.ui_element == self.backbutton:
                return "title"

        return None 
    
    def update(self, time_delta):
        self.manager.update(time_delta) #updates gui 

    def draw(self,window):
        window.fill((99, 150, 47)) 
        self.manager.draw_ui(window) # draws gui elements

