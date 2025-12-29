import subprocess
import time

"""
Maze Game Launcher
Run this: python launcher.py
"""

def launch():
	restart_count = 0
	max_restarts = 10

	print("==== Maze Game Launcher ====")

	while restart_count < max_restarts:
		if restart_count > 0:
			time.sleep(0.2)

		print("\nStarting game...")

		result = subprocess.run(["python", "main.py"])
		exit_code = result.returncode

		if exit_code == -1:
			restart_count += 1
			print("\nGame restarting...")
			continue
		elif exit_code == 0:
			print("\nGame finished.")
			break
		else:
			print(f"\nGame crashed (code: {exit_code}).")
			restart_count += 1
			continue

	print("\nThank you for playing!")

if __name__ == "__main__":
	launch()