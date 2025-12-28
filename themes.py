import pygame

__all__ = ["Theme", "THEMES", "DARK_THEME", "LIGHT_THEME", "MATRIX_THEME", "HORROR_THEME", "RETRO_THEME", "NEON_THEME", "CHRISTMAS_THEME", "HALLOWEEN_THEME"]

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
		"overlay_base": (20, 20, 25, 140),
		"player": (80, 140, 255),
		"enemy": (200, 60, 60),
		"maze": (180, 180, 180),
		"text_primary": (220, 220, 220),
		"text_secondary": (160, 160, 160),
		"text_disabled": (110, 110, 110),
		"overlay_start": (0, 0, 0, 120),
		"overlay_pause": (20, 30, 40, 150),
		"overlay_game_over": (90, 0, 0, 170),
		"overlay_game_win": (0, 60, 30, 140)
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
		"overlay_base": (220, 220, 220, 140),
		"player": (0, 120, 215),
		"enemy": (180, 40, 40),
		"maze": (60, 60, 60),
		"text_primary": (30, 30, 30),
		"text_secondary": (80, 80, 80),
		"text_disabled": (140, 140, 140),
		"overlay_start": (255, 255, 255, 160),
		"overlay_pause": (210, 210, 210, 150),
		"overlay_game_over": (160, 40, 40, 160),
		"overlay_game_win": (100, 200, 140, 140)
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
		"overlay_base": (0, 20, 0, 160),
		"player": (120, 255, 120),
		"enemy": (0, 120, 30),
		"maze": (0, 180, 50),
		"text_primary": (0, 255, 70),
		"text_secondary": (0, 180, 50),
		"text_disabled": (0, 100, 30),
		"overlay_start": (0, 40, 0, 140),
		"overlay_pause": (0, 20, 0, 170),
		"overlay_game_over": (0, 10, 0, 200),
		"overlay_game_win": (0, 80, 40, 150)
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
		"background": (10, 10, 15),
		"overlay_base": (30, 10, 10, 160),
		"player": (120, 200, 120),
		"enemy": (150, 0, 0),
		"maze": (80, 80, 80),
		"text_primary": (200, 180, 160),
		"text_secondary": (120, 120, 100),
		"text_disabled": (80, 80, 70),
		"overlay_start": (20, 20, 20, 140),
		"overlay_pause": (20, 20, 30, 150),
		"overlay_game_over": (90, 0, 0, 180),
		"overlay_game_win": (0, 50, 20, 140)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

RETRO_THEME = Theme(
	name = "retro",
	colors = {
		"background": (20, 20, 30),
		"overlay_base": (50, 50, 50, 140),
		"player": (0, 120, 215),
		"enemy": (200, 60, 60),
		"maze": (180, 180, 180),
		"text_primary": (220, 220, 220),
		"text_secondary": (160, 160, 160),
		"text_disabled": (110, 110, 110),
		"overlay_start": (30, 30, 30, 140),
		"overlay_pause": (40, 40, 40, 150),
		"overlay_game_over": (90, 0, 0, 170),
		"overlay_game_win": (0, 60, 30, 140)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

NEON_THEME = Theme(
	name = "neon",
	colors = {
		"background": (5, 5, 20),
		"overlay_base": (30, 0, 50, 160),
		"player": (0, 255, 255),
		"enemy": (255, 0, 255),
		"maze": (50, 50, 200),
		"text_primary": (255, 255, 0),
		"text_secondary": (180, 255, 0),
		"text_disabled": (100, 100, 180),
		"overlay_start": (50, 0, 50, 140),
		"overlay_pause": (50, 0, 80, 160),
		"overlay_game_over": (150, 0, 150, 180),
		"overlay_game_win": (0, 255, 100, 150)

	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

CHRISTMAS_THEME = Theme(
	name = "christmas",
	colors = {
		"background": (5, 40, 5),
		"overlay_base": (0, 0, 0, 120),
		"player": (255, 0, 0),
		"enemy": (0, 100, 0),
		"maze": (255, 255, 255),
		"text_primary": (255, 255, 0),
		"text_secondary": (200, 200, 200),
		"text_disabled": (150, 150, 150),
		"overlay_start": (0, 50, 0, 140),
		"overlay_pause": (0, 40, 0, 150),
		"overlay_game_over": (90, 0, 0, 180),
		"overlay_game_win": (255, 255, 200, 150)
	},
	fonts = {
		"large": (None, 70, False, False),
		"medium": (None, 30, False, False),
		"small": (None, 20, False, False)
	}
)

HALLOWEEN_THEME = Theme(
	name = "halloween",
	colors = {
		"background": (10, 10, 30),
		"overlay_base": (30, 10, 10, 150),
		"player": (255, 140, 0),
		"enemy": (120, 0, 0),
		"maze": (80, 80, 80),
		"text_primary": (255, 255, 100),
		"text_secondary": (160, 100, 40),
		"text_disabled": (100, 80, 50),
		"overlay_start": (20, 20, 30, 140),
		"overlay_pause": (20, 20, 20, 150),
		"overlay_game_over": (90, 0, 0, 180),
		"overlay_game_win": (100, 50, 0, 140)
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
	(HORROR_THEME.name, HORROR_THEME),
	(RETRO_THEME.name, RETRO_THEME),
	(NEON_THEME.name, NEON_THEME),
	(CHRISTMAS_THEME.name, CHRISTMAS_THEME),
	(HALLOWEEN_THEME.name, HALLOWEEN_THEME)
]