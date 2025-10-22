import pygame
import pygame_gui


class TitleScreen: 
    def __init__(self, window, manager):
        self.window = window
        self.manager = manager #creates ui manager

        self.WIDTH, self.HEIGHT = window.get_size()

        #adds title test
        self.font = pygame.font.SysFont("Arial", 96, bold = True)
        self.title = self.font.render("Untitled", True, (0,0,0))
        self.title_rect = self.title.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3 ))

        #creates log in button
        loginbutton_rect = pygame.Rect(100,150,150,45)
        self.loginbutton = pygame_gui.elements.UIButton(
            relative_rect = loginbutton_rect, 
            text = 'Log In',
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery': 'centery'}
        )

        #creates sign up button
        signupbutton_rect = pygame.Rect(-100,150,150,45)
        self.signupbutton = pygame_gui.elements.UIButton(
            relative_rect = signupbutton_rect, 
            text = 'Sign Up',
            manager = self.manager,
            anchors={'centerx': 'centerx', 'centery': 'centery'}
        )

    def handle_event(self, event): #handles input and next screen
        #handles window resizing
        if event.type == pygame.VIDEORESIZE: 
            self.WIDTH, self.HEIGHT = event.w, event.h
            self.title_rect = self.title.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 3))
            self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
            self.manager.set_window_resolution((self.WIDTH, self.HEIGHT))

        #manages button clicks
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.loginbutton: 
                return "login"      #tells main script to switch to login menu
            elif event.ui_element == self.signupbutton: 
                return "signup"     #tells main script to switch to signup menu 
        return None

    def update(self, time_delta):  
        self.manager.update(time_delta) #updates gui 

    def draw(self, window): 
        window.fill((99, 150, 47)) 
        window.blit(self.title, self.title_rect) #displays title
        self.manager.draw_ui(window) # draws gui elements
