"""contains settings class"""

class Settings: # pylint: disable=too-few-public-methods
    """A class to store all settings for game"""
    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.template_speed = 1.5
