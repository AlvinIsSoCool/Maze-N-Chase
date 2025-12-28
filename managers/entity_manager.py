import pygame
import settings

from collisions import CollisionHandler
from constants import EntityType

class EntityManager:
	def __init__(self, ctx):
		self.entities = []
		self.players = []
		self.enemies = []
		self.ctx = ctx

	def add(self, e):
		self.entities.append(e)
		if e.type == EntityType.PLAYER: self.players.append(e)
		if e.type == EntityType.ENEMY: self.enemies.append(e)

	def add_all(self, entities):
		for e in entities: 
			self.add(e)

	def remove_all(self):
		self.entities = []
		self.players = []
		self.enemies = []

	def remove_entity(self, e):
		if e in self.entities: self.entities.remove(e)
		if e in self.players: self.players.remove(e)
		if e in self.enemies: self.enemies.remove(e)

	def update(self, dt):
		for e in self.entities:
			e.update(dt)

		self.handle_entity_collisions()
		self.handle_player_win()
		self.cleanup()

	def handle_entity_collisions(self):
		if not settings.NOCLIP:
			for p in self.players:
				if not p.alive: 
					continue

				for x in self.enemies:
					if not x.alive: 
						continue
					if p.rect.colliderect(x.rect):
						print(f"P-E Collision Detected!")
						self.resolve_entity_damage(p, x)

	def handle_player_win(self):
		if not settings.NOCLIP:
			for p in self.players:
				if not p.alive: continue
				if (p.rect.left >= settings.WIDTH or p.rect.right <= 0) or (p.rect.bottom <= 0 or p.rect.top >= settings.HEIGHT):
					self.ctx.win_run()

	def resolve_entity_damage(self, p, x):
		p.damage()

	def cleanup(self):
		for e in self.entities:
			if not e.alive: self.remove_entity(e)

	def force_all_dirty(self):
		for e in self.entities:
			e.set_dirty()

	def draw(self, surface):
		dirty = False
		for e in self.entities:
			dirty |= e.draw(surface, self.ctx.maze.surface)
		return dirty

	def get_by_type(self, entity_type):
		if entity_type == EntityType.PLAYER: return self.players
		elif entity_type == EntityType.ENEMY: return self.enemies
		else: return []

	def get_all(self):
		return self.entities

	def get_player(self, n=0):
		return self.players[n]

	def get_enemy(self, n=0):
		return self.enemies[n]

	def on_theme_change(self, theme):
		for e in self.entities:
			e.on_theme_change(theme)