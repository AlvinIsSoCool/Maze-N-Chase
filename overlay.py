import pygame
import settings

from constants import GameState

class OverlayHandler:
	def __init__(self, surface, theme):
		self.surface = surface
		self.theme = theme
		self.dirty = True
		self.active = False

	def reset(self):
		self.surface.fill((0, 0, 0, 0))
		self.dirty = True
		self.active = False
		print("Overlay Reset Complete!")

	def on_state_change(self):
		self.dirty = True
		self.active = True

	def on_theme_change(self, theme):
		self.theme = theme
		self.dirty = True

	def draw(self, screen):
		if self.dirty: 
			screen.blit(self.surface, (0, 0))
			self.dirty = False
			print("Overlay Draw Complete!")
			return True
		return False

class GlobalOverlayHandler(OverlayHandler):
	def __init__(self, surface, theme):
		super().__init__(surface, theme)

	def draw_start(self):
		self.surface.fill(self.theme.color("start_screen"))

		text1 = self.theme.font("large").render("Maze N' Chase", True, self.theme.color("start_text"))
		text2 = self.theme.font("small").render("Press ENTER to continue...", True, self.theme.color("start_text"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 100))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 250))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.on_state_change()

	def draw_pause_menu(self):
		self.surface.fill(self.theme.color("pause_screen"))
		self.on_state_change()

	def draw_game_over(self):
		self.surface.fill(self.theme.color("gameover_screen"))
		text1 = self.theme.font("large").render("GAME OVER!", True, self.theme.color("accent_text"))
		text2 = self.theme.font("small").render("Press ENTER to respawn...", True, self.theme.color("accent_text"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 150))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 300))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.on_state_change()

	def draw_game_won(self):
		self.surface.fill(self.theme.color("gamewon_screen"))
		text1 = self.theme.font("large").render("GAME WON!", True, self.theme.color("accent_text"))
		text2 = self.theme.font("small").render("Press ENTER to restart...", True, self.theme.color("accent_text"))

		rect1 = text1.get_rect(center=(settings.WIDTH // 2, 150))
		rect2 = text2.get_rect(center=(settings.WIDTH // 2, 300))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.on_state_change()

class LocalOverlayHandler(OverlayHandler):
	def __init__(self, surface, theme):
		super().__init__(surface, theme)

	def draw_coordinates(self, em):
		self.surface.fill((0, 0, 0, 0))

		p, x = em.get_player(), em.get_enemy()
		px, py = p.rect.topleft
		xx, xy = x.rect.topleft
		text1 = self.theme.font("small").render(f"Player1 -> X: {px}, Y: {py}", True, self.theme.color("coordinates_text"))
		text2 = self.theme.font("small").render(f"Enemy1 -> X: {xx}, Y: {xy}", True, self.theme.color("coordinates_text"))
		rect1 = text1.get_rect(topleft=(5, 5))
		rect2 = text2.get_rect(topleft=(5, 25))

		self.surface.blit(text1, rect1)
		self.surface.blit(text2, rect2)
		self.dirty = True