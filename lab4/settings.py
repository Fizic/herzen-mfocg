class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.fps = 60

        self.player_speed = 5
        self.player_hitframes = 15
        self.jump_height = 20

        self.platform_color = (70, 0, 150)
