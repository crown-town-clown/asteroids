import pygame
from constants import *
from player import Player


def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

	while True:
		screen.fill(000000)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
				
		for item in drawable:
			item.draw(screen)
		updatable.update(dt)

		dt = game_clock.tick(60) / 1000
		pygame.display.flip()

if __name__ == "__main__":
    main()