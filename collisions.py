import settings
from constants import TOP, LEFT, BOTTOM, RIGHT

class CollisionHandler:
	@staticmethod
	def update(maze, e):
		CollisionHandler.handle_collisions_maze(maze, e)

	@staticmethod
	def handle_collisions_maze(maze, e):
		if not settings.NOCLIP:
			tile = maze.tile
			grid = maze.grid
			rows = maze.rows
			cols = maze.cols

			hs = e.size / 2
			ex, ey = e.pos.x, e.pos.y
			cx, cy = ex + hs, ey + hs
			r, c = int(cy // tile), int(cx // tile)
			pad = 1

			if 0 <= r < rows and 0 <= c < cols:
				cell = grid[r][c]
				cell_x = c * tile
				cell_y = r * tile

				if cell & TOP:
					min_y = cell_y + pad
					if ey < min_y:
						e.pos.y = min_y + pad
						e.set_collided(TOP)

				if cell & BOTTOM:
					max_y = cell_y + tile - pad
					if ey + e.size > max_y:
						e.pos.y = max_y - e.size
						e.set_collided(BOTTOM)

				if cell & LEFT:
					min_x = cell_x + pad
					if ex < min_x:
						e.pos.x = min_x + pad
						e.set_collided(LEFT)

				if cell & RIGHT:
					max_x = cell_x + tile - pad
					if ex + e.size > max_x:
						e.pos.x = max_x - e.size
						e.set_collided(RIGHT)

		e.old_rect = e.rect.copy()
		e.rect.topleft = e.pos
		if e.old_rect.topleft != e.rect.topleft: e.set_dirty()