import pygame
from constants import *


def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	dt = 0

	while True:
		screen.fill(000000)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = game_clock.tick(60) / 1000
		pygame.display.flip()

if __name__ == "__main__":
    main()