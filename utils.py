import math
import settings

def is_tile_size_valid(w, h, tile): 
	return (w % tile == 0) and (h % tile == 0)

def get_common_divisors(a, b):
	a, b = int(a), int(b)
	gcd_ab = math.gcd(a, b)
	divs_small = []
	divs_large = []

	for i in range(1, math.isqrt(gcd_ab) + 1):
		if gcd_ab % i == 0:
			divs_small.append(i)
			if i != gcd_ab // i:
				divs_large.append(gcd_ab // i)

	return divs_small + divs_large[::-1]

def get_valid_tile_size(w, h, requested_tile):
	MAX_TILE = min(w, h)
	divisors = [d for d in get_common_divisors(w, h) if settings.MIN_TILE <= d <= MAX_TILE]

	if not divisors: raise ValueError("No valid tile size available for these dimensions.")
	return min(divisors, key=lambda d: abs(d - requested_tile))

def get_grid_dimensions(w, h, requested_tile):
	if is_tile_size_valid(w, h, requested_tile): tile = requested_tile
	else: tile = get_valid_tile_size(w, h, requested_tile)

	rows = h // tile
	cols = w // tile
	return rows, cols, tile

def clamp(in_val, min_val, max_val):
	return max(min_val, min(in_val, max_val))