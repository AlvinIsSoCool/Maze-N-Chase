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
		"background": (0, 0, 0),
		"maze": (255, 255, 255),
		"player": (255, 255, 255),
		"enemy": (0, 0, 255),
		"start_screen": (0, 0, 0, 255),
		"pause_screen": (0, 0, 0, 100),
		"gameover_screen": (255, 0, 0, 150),
		"gamewon_screen": (0, 255, 0, 150),
		"start_text": (255, 255, 255),
		"accent_text": (0, 0, 0),
		"coordinates_text": (0, 0, 255)
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
		"background": (255, 255, 255),
		"maze": (0, 0, 0),
		"player": (0, 0, 0),
		"enemy": (0, 0, 255),
		"start_screen": (255, 255, 255, 255),
		"pause_screen": (0, 0, 0, 100),
		"gameover_screen": (255, 0, 0, 150),
		"gamewon_screen": (0, 255, 0, 150),
		"start_text": (0, 0, 0),
		"accent_text": (255, 255, 255),
		"coordinates_text": (0, 0, 255)
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
		"background": (0, 0, 0),
		"maze": (0, 255, 120),
		"player": (0, 255, 70),
		"enemy": (0, 0, 255),
		"start_screen": (0, 0, 0, 255),
		"pause_screen": (0, 0, 0, 100),
		"gameover_screen": (255, 0, 0, 150),
		"gamewon_screen": (0, 255, 0, 150),
		"start_text": (255, 255, 255),
		"accent_text": (255, 255, 255),
		"coordinates_text": (0, 0, 255)
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