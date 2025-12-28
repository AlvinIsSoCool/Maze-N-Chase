import pygame
import random
import settings

from .entity import Entity
from constants import EntityType, TOP, LEFT, BOTTOM, RIGHT, OPPOSITE, DIR_MASK

class Enemy(Entity):
	def __init__(self, ctx, x=None, y=None, speed=150, size=8, color=(0, 0, 0)):
		x = random.randint(0, settings.WIDTH - size)
		y = random.randint(0, settings.HEIGHT - size)
		self.type = EntityType.ENEMY
		self.direction = random.choice([TOP, LEFT, BOTTOM, RIGHT])
		self.blocked_wall = None
		self.collided = False

		super().__init__(ctx, self.type, x, y, speed, size, color)

	def update(self, dt):
		if not self.alive:
			return

		if self.direction is None or self.collided:
			self.choose_new_direction()
			self.collided = False

		dx, dy = DIR_MASK[self.direction]

		if dx == 0 and dy == 0:
			return

		move = self.speed * dt
		self.old_rect = self.rect.copy()

		if dx != 0: 
			self.rect.x += dx * move
		elif dy != 0: 
			self.rect.y += dy * move

		CollisionHandler.handle_collisions_maze(self.ctx.maze, self)

		if self.rect.topleft != self.old_rect.topleft: 
			self.set_dirty()

	def choose_new_direction(self):
		available = []

		for direction in (TOP, LEFT, BOTTOM, RIGHT):
			if self.blocked_wall & direction: 
				continue
			if direction == OPPOSITE[self.direction]: 
				continue
			available.append(direction)

		if not available: 
			available = [OPPOSITE[self.direction]]
		self.direction = random.choice(available)

	def set_collided(self, blocked_wall):
		self.collided = True
		self.blocked_wall = blocked_wall

	def on_theme_change(self, theme):
		self.color = theme.color("enemy")
		self.dirty = True