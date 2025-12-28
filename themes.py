import pygame

__all__ = ["Theme", "THEMES", "DARK_THEME", "LIGHT_THEME", "MATRIX_THEME", "HORROR_THEME"]

class Theme:
	def __init__(self, *, name, colors, fonts):
		self.name = name
		self.colors = colors
		self.font_defs = fonts
		self._fonts = {}

	def color(self, key):
		return self.colors[key]

	def font(self, key):
		if key not in self._fonts:
			path, size, bold, italic = self.font_defs[key]
			font = pygame.font.Font(path, size)
			font.set_bold(bold)
			font.set_italic(italic)
			self._fonts[key] = font
		return self._fonts[key]

DARK_THEME = Theme(
	name = "dark",
	colors = {
		"background": (15, 15, 18),
		"maze": (180, 180, 180),
		"player": (80, 140, 255),
		"enemy": (200, 60, 60),
		"overlay_base": (20, 20, 22, 140),
		"start_screen": (0, 0, 0, 120),
		"pause_screen": (20, 30, 40, 150),
		"gameover_screen": (90, 0, 0, 170),
		"gamewon_screen": (0, 60, 30, 140),
		"primary_text": (220, 220, 220),
		"secondary_text": (160, 160, 160),
		"disabled_text": (110, 110, 110)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

LIGHT_THEME = Theme(
	name = "light",
	colors = {
		"background": (245, 245, 245),
		"maze": (60, 60, 60),
		"player": (0, 120, 215),
		"enemy": (180, 40, 40),
		"overlay_base": (220, 220, 220, 140),
		"start_screen": (255, 255, 255, 160),
		"pause_screen": (210, 210, 210, 150),
		"gameover_screen": (160, 40, 40, 160),
		"gamewon_screen": (100, 200, 140, 140),
		"primary_text": (30, 30, 30),
		"secondary_text": (80, 80, 80),
		"disabled_text": (140, 140, 140)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)


MATRIX_THEME = Theme(
	name = "matrix",
	colors = {
		"background": (5, 10, 5),
		"maze": (0, 180, 50),
		"player": (120, 255, 120),
		"enemy": (0, 120, 30),
		"overlay_base": (0, 20, 0, 160),
		"start_screen": (0, 40, 0, 140),
		"pause_screen": (0, 20, 0, 170),
		"gameover_screen": (0, 10, 0, 200),
		"gamewon_screen": (0, 80, 40, 150),
		"primary_text": (0, 255, 70),
		"secondary_text": (0, 180, 50),
		"disabled_text": (0, 100, 30)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

HORROR_THEME = Theme(
	name = "horror",
	colors = {
		"background": (150, 5, 5),
		"maze": (255, 0, 0),
		"player": (0, 0, 0),
		"enemy": (50, 0, 80),
		"start_screen": (255, 0, 0, 255),
		"pause_screen": (0, 0, 0, 100),
		"gameover_screen": (255, 0, 0, 150),
		"gamewon_screen": (0, 255, 0, 150),
		"start_text": (0, 0, 0),
		"accent_text": (0, 0, 0),
		"coordinates_text": (0, 0, 255)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

THEMES = [
	(DARK_THEME.name, DARK_THEME),
	(LIGHT_THEME.name, LIGHT_THEME),
	(MATRIX_THEME.name, MATRIX_THEME),
	(HORROR_THEME.name, HORROR_THEME)
]
