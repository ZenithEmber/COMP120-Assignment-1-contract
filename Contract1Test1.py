import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # this line of code creates a display window which lets the user see what the program is doing.
pygame.display.set_caption("Contract 1 Tile Generator")
clock = pygame.time.Clock()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

Tiles = ("grass", "stone", "sand", "Grass", "Stone", "Sand") #this is the list of tiles which the user may input to get a solid colour box.

Grass_color = 0, 204, 0
Stone_color = 128, 128, 128
Sand_color = 218, 183, 12
#these values determine the colour of the tile, it is RGB(Red, Green, Blue). There is a max value of 255 in each colour or in hexadecimal, it is known as FF.

tile = str(input("Enter which tile you would like, selection is: Grass, Stone, Sand: ")) #this line of code is waiting for the user to input a string, while it is waiting it prints out the message between the speech marks.

tile.lower

if tile in Tiles:
	while True: #this is a basic iteration
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # this line of code determines whether the user has clicked the exit button in the top right, without this code the user wouldn't be able to close the program.
				running = False
				screen.fill(BLACK)

			if tile == "sand":
				pygame.draw.rect(screen, Sand_color, (10, 10, 50, 50))
			elif tile == "stone":
				pygame.draw.rect(screen, Stone_color, (10, 10, 50, 50))
			elif tile == "grass":
				pygame.draw.rect(screen, Grass_color, (10, 10, 50, 50))
			else:
				pygame.draw.rect(screen, WHITE, (10, 10, 50, 50)) #these numbers in brackets add a padding and set the size of the box. As well as the WHITE colour, the others call the RGB values which are assigned to each different tile.

			pygame.display.flip()
	
	sys.exit() #this line of code exits the program when the user wants to stop using the program.
