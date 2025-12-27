import pygame
import sys
import settings
import utils

from overlay import GlobalOverlayHandler
from constants import GameState
from ctx import GameContext
from themes import *
from managers import ThemeManager

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH + 1, settings.HEIGHT + 1))
		self.screen.fill((0, 0, 0))

		self.fps = settings.FPS
		self.max_dt = 1 / 60
		self.real_dt = None
		self.sim_dt = None

		self.clock = pygame.time.Clock()
		self.running = True
		self.state = None
		self.theme_mgr = ThemeManager(THEMES, "light")
		print(self.theme_mgr.theme.name)
		self.overlay_global = GlobalOverlayHandler(pygame.Surface((settings.WIDTH + 1, settings.HEIGHT + 1), pygame.SRCALPHA).convert_alpha(), self.theme_mgr.theme)
		self.ctx = GameContext(self, self.theme_mgr.theme)

		self.set_state(GameState.START)
		self.dirty = True

		# DEBUG
		self.frame_count = 0
		self.update_count = 0
		self.draw_count = 0
		self.event_count = 0

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q: self.end_game()
				if event.key == pygame.K_RETURN:
					if self.state == GameState.START: self.set_state(GameState.PLAYING, True)
					elif self.state == GameState.GAMEOVER or self.state == GameState.GAMEWON: self.ctx.restart_run()
				if event.key == pygame.K_ESCAPE:
					if self.state == GameState.PLAYING: self.set_state(GameState.PAUSED, True)
					elif self.state == GameState.PAUSED: self.set_state(GameState.PLAYING, True)
				if event.key == pygame.K_t:
					self.change_theme(self.theme_mgr.next_theme())
					print(self.theme_mgr.theme.name)

			if event.type == pygame.WINDOWFOCUSLOST:
				print("Window lost focus.")
				self.set_state(GameState.PAUSED)
				self.fps /= 4

			if event.type == pygame.WINDOWFOCUSGAINED:
				print("Window gained focus.")
				self.fps = settings.FPS

			if event.type == pygame.WINDOWMINIMIZED:
				print("Window minimized.")
				self.set_state(GameState.PAUSED)
				self.fps /= 4

			if event.type == pygame.WINDOWRESTORED:
				print("Window restored.")
				self.ctx.force_all_dirty()
				self.overlay_global.dirty = True

			self.ctx.handle_event(event)
			self.event_count += 1
			#print(f"Event Count: {self.event_count}")

	# TODO: Add overlay logic.
	def update(self, dt):
		"""if self.state == GameState.START: 
			pass
		elif self.state == GameState.MENU: 
			pass
		elif self.state == GameState.PAUSED:
			pass
		elif self.state == GameState.PLAYING:
			self.ctx.update(dt)
		elif self.state == GameState.GAMEWON:
			pass
		elif self.state == GameState.GAMEOVER:
			pass"""

		if self.state == GameState.PLAYING:
			self.ctx.update(dt)
			self.update_count += 1
			#print(f"Update Count: {self.update_count}")

	def draw(self):
		if self.state != GameState.START:
			self.dirty |= self.ctx.draw()

		self.dirty |= self.overlay_global.draw(self.screen)

		if self.dirty:
			pygame.display.flip()
			self.dirty = False
			self.draw_count += 1
			#print(f"Draw Count: {self.draw_count}")

	def set_state(self, state, force=False):
		if (state != self.state and isinstance(state, GameState)) and (force or not self.overlay_global.active):
			self.state = state
			self.ctx.force_all_dirty()
			self.overlay_global.reset()

			if self.state == GameState.START: self.overlay_global.draw_start()
			elif self.state == GameState.PAUSED: self.overlay_global.draw_pause_menu()
			elif self.state == GameState.GAMEOVER: self.overlay_global.draw_game_over()
			elif self.state == GameState.GAMEWON: self.overlay_global.draw_game_won()

	def change_theme(self, theme):
		if self.theme_mgr.set_theme(theme):
			self.overlay_global.on_theme_change(theme)
			self.ctx.on_theme_change(theme)

	def end_game(self):
		self.running = False

	def restart_game(self):
		# Actual restarting of the game happens here.
		pass

	# TODO: Throttle or prevent updates when window loses focus.
	def run(self):
		while self.running:
			self.real_dt = self.clock.tick(self.fps) / 1000
			self.sim_dt = min(self.real_dt, self.max_dt)

			self.handle_events()
			self.update(self.sim_dt)
			self.draw()
			self.frame_count += 1

		pygame.quit()
		sys.exit()