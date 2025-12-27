import pygame

class Entity:
	def __init__(self, ctx, entity_type, x, y, speed, size, color):
		self.ctx = ctx
		self.type = entity_type
		self.x = x
		self.y = y
		self.speed = speed
		self.size = size
		self.color = color
		self.pos = pygame.Vector2(self.x, self.y)
		self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
		self.old_rect = self.rect.copy()
		self.alive = True
		self.dirty = True

	def update(self, dt):
		pass

	def set_dirty(self):
		self.dirty = True

	def draw(self, screen, back):
		if self.alive and self.dirty:
			screen.blit(back, self.old_rect, self.old_rect)
			pygame.draw.rect(screen, self.color, self.rect)
			self.dirty = False
			return True
		return False

	def damage(self):
		self.alive = False

	def set_collided(self, blocked_wall):
		pass

	def on_theme_change(self, theme):
		pass