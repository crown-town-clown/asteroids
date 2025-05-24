import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from shot import Shot


def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# set up screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	game_clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	player1 = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	field = AsteroidField()

	while True:
		screen.fill(000000)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for item in drawable:
			item.draw(screen)
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.check_collision(player1):
				sys.exit("Game over!")
			for shot in shots:
				if shot.check_collision(asteroid):
					shot.kill()
					asteroid.split()

		dt = game_clock.tick(60) / 1000
		pygame.display.flip()

if __name__ == "__main__":
    main()