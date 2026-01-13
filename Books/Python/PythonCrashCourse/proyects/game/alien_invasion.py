import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock() # Initialize the game clock 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # Set the screen size
        
        pygame.display.set_caption("Alien Invasion") # Set the window title
        self.ship = Ship(self) # Create an instance of Ship
        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True: # Main loop for the game
            self._check_events()
            self.update_screen()
            self.clock.tick(60)  # Limit the frame rate to 60 frames per second


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color) # Fill the screen with the background color
        self.ship.blitme() # Draw the ship on the screen
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
