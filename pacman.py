import pygame, random

'''
The Pacman class is designed to represent the Pacman character in the game.
It includes methods to draw Pacman on the screen, move Pacman in different directions, and relocate Pacman to a random position. 
There are also a series of getters to access private instance variables such as 'x' and 'y' coordinates, radius, and colour
The class also includes a string representation method to display Pacman's colour and coordinates.
'''

class Pacman:

    def __init__(self, x, y, radius, colour, speed): #Initialises the Pacman object
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__colour = colour
        self.__speed = speed

    def draw(self, display): #Draws Pacman on the screen
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius)

    def get_x(self): #Returns the x coordinate
        return self.__x

    def get_y(self): #Returns the y coordinate
        return self.__y
    
    def get_radius(self): #Returns the radius
        return self.__radius
    
    def get_colour(self): #Returns the colour of Pacman
        return self.__colour
    
    def move_down(self): #Moves Pacman down and ensures when he leaves one side of the frame he appears at the opposite side
        self.__y += self.__speed
        if self.__y >= 485:
            self.__y = -19

    def move_up(self): #Moves Pacman up and ensures when he leaves one side of the frame he appears at the opposite side
        self.__y -= self.__speed
        if self.__y <= -19:
            self.__y = 485

    def move_right(self): #Moves Pacman right and ensures when he leaves one side of the frame he appears at the opposite side
        self.__x += self.__speed
        if self.__x >= 619:
            self.__x = -19

    def move_left(self): #Moves Pacman left and ensures when he leaves one side of the frame he appears at the opposite side
        self.__x -= self.__speed
        if self.__x <= -19:
            self.__x = 619

    def relocate(self, display_width, display_height): #Relocates Pacman to a random position within the display boundaries.
        self.__x = random.randint(0, display_width - self.__radius)
        self.__y = random.randint(0, display_height - self.__radius)
    
    def __str__(self): #Returns a string representation of Pacman's color and coordinates.
        return f"Pacman: Colour={self.__colour}, Coordinates=({self.__x}, {self.__y})"

