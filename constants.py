from enum import Enum, auto

class EntityType(Enum):
	PLAYER = auto()
	ENEMY = auto()

class GameState(Enum):
	START = auto()
	PLAYING = auto()
	PAUSED = auto()
	GAME_WIN = auto()
	GAME_OVER = auto()

TOP = 1 << 0
LEFT = 1 << 1
BOTTOM = 1 << 2
RIGHT = 1 << 3

FULL = TOP | LEFT | BOTTOM | RIGHT
DIRECTIONS = [TOP, LEFT, BOTTOM, RIGHT]

DX = {
	TOP: 0,
	LEFT: -1,
	BOTTOM: 0,
	RIGHT: 1
}

DY = {
	TOP: -1,
	LEFT: 0,
	BOTTOM: 1,
	RIGHT: 0
}

OPPOSITE = {
	TOP: BOTTOM,
	LEFT: RIGHT,
	BOTTOM: TOP,
	RIGHT: LEFT
}

DIR_MASK = {
	TOP: (0,-1),
	LEFT: (-1,0),
	BOTTOM: (0,1),
	RIGHT: (1,0)
}