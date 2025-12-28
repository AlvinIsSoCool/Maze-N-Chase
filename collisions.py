import settings
from constants import TOP, LEFT, BOTTOM, RIGHT

class CollisionHandler:
	@staticmethod
	def handle_collisions_maze(maze, e):
		if settings.NOCLIP:
			return

		tile = maze.tile
		grid = maze.grid
		rows = maze.rows
		cols = maze.cols

		cx, cy = e.rect.center
		r, c = int(cy // tile), int(cx // tile)

		if not (0 <= r < rows and 0 <= c < cols):
			return

		cell = grid[r][c]
		cell_x = c * tile
		cell_y = r * tile

		dx = e.rect.x - e.old_rect.x
		dy = e.rect.y - e.old_rect.y

		if dx != 0:
			if dx > 0 and (cell & RIGHT):
				wall_x = cell_x + tile
				if e.rect.right > wall_x:
					e.rect.right = wall_x
					e.set_collided(RIGHT)

			elif dx < 0 and (cell & LEFT):
				wall_x = cell_x
				if e.rect.left < wall_x:
					e.rect.left = wall_x
					e.set_collided(LEFT)

		if dy != 0:
			if dy > 0 and (cell & BOTTOM):
				wall_y = cell_y + tile
				if e.rect.bottom > wall_y:
					e.rect.bottom = wall_y
					e.set_collided(BOTTOM)

			elif dy < 0 and (cell & TOP):
				wall_y = cell_y
				if e.rect.top < wall_y:
					e.rect.top = wall_y
					e.set_collided(TOP)