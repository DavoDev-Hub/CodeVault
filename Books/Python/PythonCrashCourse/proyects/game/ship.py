import pygame

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Books/Python/PythonCrashCourse/proyects/game/images/ship.bmp')
        self.rect = self.image.get_rect() # Get the rectangular area of the image

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ship's horizontal position
        self.x = float(self.rect.x)


        # Movement flag; start with a ship that is not moving.
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ Update the ship's position based on movement flags. """
        if self.moving_right:
            self.x += self.settings.ship_speed  # Move the ship to the right
        if self.moving_left:
            self.x -= self.settings.ship_speed  # Move the ship to the left

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)

