import pygame
import random
import settings

from .entity import Entity
from constants import EntityType

class Player(Entity):
	def __init__(self, ctx, x=None, y=None, speed=200, size=8, color=(0, 0, 0)):
		x = random.randint(0, settings.WIDTH - size)
		y = random.randint(0, settings.HEIGHT - size)
		self.type = EntityType.PLAYER
		super().__init__(ctx, self.type, x, y, speed, size, color)

	def update(self, dt):
		if not self.alive:
			return

		keys = pygame.key.get_pressed()
		dx = dy = 0

		if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
			dx = 1
		elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
			dx = -1
		elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
			dy = 1
		elif keys[pygame.K_w] or keys[pygame.K_UP]:
			dy = -1

		if dx == 0 and dy == 0:
			return

		move = self.speed * dt
		self.old_rect = self.rect.copy()
		self.rect.x += dx * move
		self.rect.y += dy * move
		
		CollisionHandler.handle_collisions_maze(maze, self)

		if self.rect.topleft != self.old_rect.topleft:
			self.set_dirty()

	def damage(self):
		super().damage()
		print("Player Damaged!")
		self.ctx.end_run()

	def set_collided(self, blocked_wall):
		pass

	def on_theme_change(self, theme):
		self.color = theme.color("player")
		self.dirty = True