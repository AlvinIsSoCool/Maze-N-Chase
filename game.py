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
		"""
		Physics System Constants:

		- PHYSICS_FPS = 60: Physics updates per second.
		- MAX_UPDATES_PER_FRAME = 10: Prevents "spiral of death" on slow hardware.
		- MAX_FRAME_TIME = 0.25: Caps frames at 250ms (4 FPS min) for stability.
		- BEHIND_RESET_THRESHOLD = 5: Reset accumulator if more than 5 updates behind.

		These values are tuned for stability. DO NOT RECONFIGURE!
		"""
		self.PHYSICS_FPS = 60
		self.MAX_UPDATES_PER_FRAME = 10
		self.MAX_FRAME_TIME = 0.25
		self.BEHIND_RESET_THRESHOLD = 5

		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH + 1, settings.HEIGHT + 1))
		self.screen.fill((0, 0, 0))

		self.fps = settings.FPS
		self.physics_dt = 1.0 / self.PHYSICS_FPS
		self.accumulator = 0.0

		self.clock = pygame.time.Clock()
		self.running = True
		self.exit_code = 0
		self.state = None
		self.theme_mgr = ThemeManager(THEMES, "light")
		print(self.theme_mgr.theme.name)
		self.overlay_global = GlobalOverlayHandler(pygame.Surface((settings.WIDTH + 1, settings.HEIGHT + 1), pygame.SRCALPHA).convert_alpha(), self.theme_mgr.theme)
		self.ctx = GameContext(self, self.theme_mgr.theme)

		self.set_state(GameState.START)
		self.dirty = True

		self.frame_count = 0
		self.update_count = 0
		self.draw_count = 0
		self.event_count = 0

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q: 
					if self.state != GameState.PLAYING: self.end_game()
				if event.key == pygame.K_RETURN:
					if self.state == GameState.START: self.set_state(GameState.PLAYING, True)
					elif self.state == GameState.GAME_OVER or self.state == GameState.GAME_WIN: self.ctx.restart_run()
				if event.key == pygame.K_ESCAPE:
					if self.state == GameState.PLAYING: self.set_state(GameState.PAUSED, True)
					elif self.state == GameState.PAUSED: self.set_state(GameState.PLAYING, True)
				
				# Temporary Placements.
				if event.key == pygame.K_t:
					self.change_theme(self.theme_mgr.next_theme())
					print(self.theme_mgr.theme.name)
				if event.key == pygame.K_r:
					self.restart_game()

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

	def update(self, dt):
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

	def set_state(self, state, force=False, refresh=False):
		if (state != self.state and isinstance(state, GameState)) and (force or not self.overlay_global.active) or refresh:
			self.state = state
			self.ctx.force_all_dirty()
			self.overlay_global.reset()
			print("State changed.")

			if self.state == GameState.START: self.overlay_global.draw_start()
			elif self.state == GameState.PAUSED: self.overlay_global.draw_pause_menu()
			elif self.state == GameState.GAME_OVER: self.overlay_global.draw_game_over()
			elif self.state == GameState.GAME_WIN: self.overlay_global.draw_game_won()

	def change_theme(self, theme):
		if self.theme_mgr.set_theme(theme):
			self.overlay_global.on_theme_change(theme)
			self.set_state(self.state, True, True)
			self.ctx.on_theme_change(theme)

	def end_game(self, exit_code=0):
		self.running = False
		self.exit_code = exit_code

	def restart_game(self):
		self.end_game(-1)

	def run_game(self):
		while self.running:
			raw_frame_time = self.clock.tick(self.fps) / 1000.0
			frame_time = min(raw_frame_time, self.MAX_FRAME_TIME)
			self.accumulator += frame_time

			self.handle_events()

			updates_done = 0
			while (self.accumulator >= self.physics_dt and 
				   updates_done < self.MAX_UPDATES_PER_FRAME):
				self.update(self.physics_dt)
				self.accumulator -= self.physics_dt
				updates_done += 1

			if self.accumulator > self.physics_dt * self.BEHIND_RESET_THRESHOLD:
				self.accumulator = self.physics_dt

			self.draw()

			# DEBUG.
			if updates_done > 1:
				print(f"Slow frame: Did {updates_done} physics update(s)")

			self.frame_count += 1

	def run(self):
		try:
			self.run_game()

		except (SystemExit, KeyboardInterrupt):
			if isinstance(e, SystemExit):
				raise
			else:
				print("\nGame interrupted")
				self.exit_code = 0

		except BaseException as e:
			print(f"\n{'='*60}")
			print("UNEXPECTED GAME TERMINATION")
			print(f"Error type: {type(e).__name__}")
			print(f"Error message: {e}")
			print("Stack trace:")
			import traceback
			traceback.print_exc()
			print(f"{'='*60}\n")

			self.exit_code = 1

		finally:
			pygame.quit()
			sys.exit(self.exit_code)