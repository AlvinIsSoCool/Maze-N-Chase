import settings
from constants import TOP, LEFT, BOTTOM, RIGHT, OPPOSITE

class CollisionHandler:
	@staticmethod
	def handle_collisions_maze(maze, e):
		if settings.NOCLIP:
			return

		tile = maze.tile
		grid = maze.grid
		rows = maze.rows
		cols = maze.cols

		# Calculate movement vector
		dx = e.rect.x - e.old_rect.x
		dy = e.rect.y - e.old_rect.y
		
		if dx == 0 and dy == 0:
			return

		# Store the proposed new position
		new_x, new_y = e.rect.x, e.rect.y
		
		# 1. Cap maximum movement per frame (prevents tunneling)
		max_move = tile // 2  # Never move more than half a tile per frame
		if abs(dx) > max_move:
			dx = max_move if dx > 0 else -max_move
			new_x = e.old_rect.x + dx
			
		if abs(dy) > max_move:
			dy = max_move if dy > 0 else -max_move
			new_y = e.old_rect.y + dy

		# 2. Check multiple points around the entity (lightweight)
		blocked_wall = 0
		
		# For horizontal movement
		if dx != 0:
			step = 1 if dx > 0 else -1
			test_x = new_x + (e.rect.width if step > 0 else 0)  # Test leading edge
			
			# Get vertical range to test (top, middle, bottom)
			test_points_y = [new_y, new_y + e.rect.height // 2, new_y + e.rect.height - 1]
			
			for test_y in test_points_y:
				r = max(0, min(rows - 1, int(test_y // tile)))
				c = max(0, min(cols - 1, int(test_x // tile)))
				
				if step > 0 and (grid[r][c] & RIGHT):
					# Check if we would cross the wall
					wall_x = (c + 1) * tile
					if test_x >= wall_x - 1:  # -1 for safety margin
						new_x = wall_x - e.rect.width - 1
						blocked_wall |= RIGHT
						break
				elif step < 0 and (grid[r][c] & LEFT):
					wall_x = c * tile
					if test_x <= wall_x + 1:  # +1 for safety margin
						new_x = wall_x + 1
						blocked_wall |= LEFT
						break

		# For vertical movement
		if dy != 0:
			step = 1 if dy > 0 else -1
			test_y = new_y + (e.rect.height if step > 0 else 0)  # Test leading edge
			
			# Get horizontal range to test (left, middle, right)
			test_points_x = [new_x, new_x + e.rect.width // 2, new_x + e.rect.width - 1]
			
			for test_x in test_points_x:
				r = max(0, min(rows - 1, int(test_y // tile)))
				c = max(0, min(cols - 1, int(test_x // tile)))
				
				if step > 0 and (grid[r][c] & BOTTOM):
					wall_y = (r + 1) * tile
					if test_y >= wall_y - 1:  # -1 for safety margin
						new_y = wall_y - e.rect.height - 1
						blocked_wall |= BOTTOM
						break
				elif step < 0 and (grid[r][c] & TOP):
					wall_y = r * tile
					if test_y <= wall_y + 1:  # +1 for safety margin
						new_y = wall_y + 1
						blocked_wall |= TOP
						break

		# 3. Apply the safe position
		e.rect.x = int(new_x)
		e.rect.y = int(new_y)
		
		# 4. Final safety check - ensure we're not stuck in a wall
		# Get the cell we're currently in
		center_r = int((e.rect.y + e.rect.height // 2) // tile)
		center_c = int((e.rect.x + e.rect.width // 2) // tile)
		
		if 0 <= center_r < rows and 0 <= center_c < cols:
			cell = grid[center_r][center_c]
			
			# Push out of walls if somehow stuck
			if cell & LEFT and e.rect.left < center_c * tile:
				e.rect.left = center_c * tile + 1
			if cell & RIGHT and e.rect.right > (center_c + 1) * tile:
				e.rect.right = (center_c + 1) * tile - 1
			if cell & TOP and e.rect.top < center_r * tile:
				e.rect.top = center_r * tile + 1
			if cell & BOTTOM and e.rect.bottom > (center_r + 1) * tile:
				e.rect.bottom = (center_r + 1) * tile - 1

		# Only trigger collision if we actually blocked movement
		if blocked_wall and (e.rect.topleft == e.old_rect.topleft):
			e.set_collided(blocked_wall)