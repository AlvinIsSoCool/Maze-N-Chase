import pygame
import random
from constants import TOP, LEFT, BOTTOM, RIGHT, FULL, DX, DY, OPPOSITE

class Maze:
	def __init__(self, rows, cols, tile, surface, theme):
		self.rows = rows
		self.cols = cols
		self.tile = tile
		self.surface = surface
		self.theme = theme
		self.grid = None
		self.visited = None
		self.dirty = True

	def on_theme_change(self, theme):
		self.theme = theme
		self.dirty = True

	def init(self): 
		self.grid = [[FULL for _ in range(self.cols)] for _ in range(self.rows)]
		self.visited = [[False]*self.cols for _ in range(self.rows)]

	def draw(self, screen):
		if self.dirty: 
			screen.blit(self.surface, (0, 0))
			self.dirty = False
			return True
		return False

	def generate_and_draw_maze_dfs(self):
		self.init()
		stack = []
		r, c = random.randrange(self.rows), random.randrange(self.cols)
		self.visited[r][c] = True
		stack.append((r, c))

		while stack:
			r, c = stack[-1]
			neighbors = []

			for direction in (TOP, RIGHT, BOTTOM, LEFT):
				nr = r + DY[direction]
				nc = c + DX[direction]

				if 0 <= nr < self.rows and 0 <= nc < self.cols:
					if not self.visited[nr][nc]:
						neighbors.append((direction, nr, nc))

			if not neighbors:
				stack.pop()
				continue

			direction, nr, nc = random.choice(neighbors)
			self.grid[r][c] ^= direction
			self.grid[nr][nc] ^= OPPOSITE[direction]

			self.visited[nr][nc] = True
			stack.append((nr, nc))

		self.draw_maze()

	def generate_and_draw_grid(self):
		self.init()
		self.draw_maze()

	def draw_maze(self):
		self.surface.fill(self.theme.color("background"))
		rows = len(self.grid)
		cols = len(self.grid[0])

		for r in range(rows):
			for c in range(cols):
				x, y = c * self.tile, r * self.tile
				cell = self.grid[r][c]

				if cell & TOP: pygame.draw.line(self.surface, self.theme.color("maze"), (x, y), (x+self.tile, y))
				if cell & LEFT: pygame.draw.line(self.surface, self.theme.color("maze"), (x, y), (x, y+self.tile))
				if cell & RIGHT: pygame.draw.line(self.surface, self.theme.color("maze"), (x+self.tile, y), (x+self.tile, y+self.tile))
				if cell & BOTTOM: pygame.draw.line(self.surface, self.theme.color("maze"), (x, y+self.tile), (x+self.tile, y+self.tile))

		self.dirty = True