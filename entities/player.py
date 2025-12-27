import pygame

from .entity import Entity
from constants import EntityType

class Player(Entity):
	def __init__(self, ctx, x=100, y=100, speed=300, size=8, color=(0, 0, 0)):
		self.type = EntityType.PLAYER
		super().__init__(ctx, self.type, x, y, speed, size, color)

	def update(self, dt):
		if self.alive:
			keys = pygame.key.get_pressed()
			direction = pygame.Vector2(0, 0)

			if keys[pygame.K_RIGHT]: direction.update(1, 0)
			elif keys[pygame.K_LEFT]: direction.update(-1, 0)
			elif keys[pygame.K_DOWN]: direction.update(0, 1)
			elif keys[pygame.K_UP]: direction.update(0, -1)

			if direction.length_squared() == 0: return

			movement = direction * (self.speed * dt)
			self.pos += movement

	def damage(self):
		super().damage()
		print("Player Damaged!")
		self.ctx.end_run()

	def set_collided(self, blocked_wall):
		pass

	def on_theme_change(self, theme):
		self.color = theme.color("player")
		self.dirty = True