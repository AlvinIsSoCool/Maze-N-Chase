import pygame
import random
import settings
import utils

from maze import Maze
from entities import Player, Enemy
from managers import EntityManager
from overlay import LocalOverlayHandler
from constants import GameState
from themes import *

class GameContext:
	def __init__(self, game, theme):
		self.game = game
		self.screen = self.game.screen
		self.theme = theme
		rows, cols, tile = utils.get_grid_dimensions(settings.WIDTH, settings.HEIGHT, settings.TILE_SIZE)
		print(f"Rows: {rows}, Columns: {cols}, Tile: {tile}")

		self.maze = Maze(rows + 1, cols + 1, tile, pygame.Surface((settings.WIDTH + 1, settings.HEIGHT + 1)).convert(), theme)
		self.maze.generate_and_draw_maze_dfs()
		#self.maze.generate_and_draw_grid()

		self.em = EntityManager(self)
		player = Player(self, color=self.theme.color("player"))
		enemy = Enemy(self, color=self.theme.color("enemy"))

		self.em.add_all([player, enemy])

		self.overlay_ctx = LocalOverlayHandler(pygame.Surface((settings.WIDTH + 1, settings.HEIGHT + 1), pygame.SRCALPHA).convert_alpha(), theme)

	def handle_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				if settings.NOCLIP: settings.NOCLIP = False
				elif not settings.NOCLIP: settings.NOCLIP = True

	def update(self, dt):
		self.em.update(dt)

	def draw(self):
		dirty = False

		dirty |= self.maze.draw(self.screen)
		dirty |= self.em.draw(self.screen)
		#self.overlay_ctx.draw_coordinates(self.em)
		dirty |= self.overlay_ctx.draw(self.screen)
		return dirty

	def end_run(self):
		self.game.set_state(GameState.GAME_OVER)

	def win_run(self):
		self.game.set_state(GameState.GAME_WIN)

	def restart_run(self, full=True):
		self.em.remove_all()
		player = Player(self, color=self.theme.color("player"))
		enemy = Enemy(self, color=self.theme.color("enemy"))

		self.game.set_state(GameState.PLAYING, True)
		if full:
			self.maze.generate_and_draw_maze_dfs()
		self.em.add_all([player, enemy])

	def force_all_dirty(self):
		self.maze.dirty = True
		self.overlay_ctx.dirty = True
		self.em.force_all_dirty()

	def on_theme_change(self, theme):
		self.theme = theme

		self.overlay_ctx.on_theme_change(theme)
		self.maze.on_theme_change(theme)
		self.em.on_theme_change(theme)