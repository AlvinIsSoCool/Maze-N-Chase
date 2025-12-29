import game
import sys

def main():
	try:
		g = game.Game()
		g.run()
	except SystemExit as e:
		sys.exit(e.code)

if __name__ == "__main__":
	main()