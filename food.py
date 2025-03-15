import pygame, random

'''
The Food class is designed to represent the Food in the game.
It includes methods to draw the Food on the screen and relocate it to a random position. 
There are also a series of getters to access private instance variables such as 'x' and 'y' coordinates, height and width, and colour
The class also includes a string representation method to display the Food's colour and coordinates.
'''

class Food:
    #Class variables are defined which are the same across the different instances of the food class instantiated
    __colour = [255, 255, 255]
    __width = 15
    __height = 15

    def __init__(self, x, y): #Initialises the food object with its position which is unique for each instance
        self.__x = x
        self.__y = y
    
    def draw(self, display): #Draws the Food to a screen
        pygame.draw.rect(display, self.__colour, [self.__x, self.__y, self.__width, self.__height])
    
    def relocate(self, display_width, display_height): #Relocates the food to a random position within the display boundaries
        self.__x = random.randint(0, display_width - self.__width)
        self.__y = random.randint(0, (display_height - 100) - self.__height)

    def get_x(self): #Returns the x coordinate
        return self.__x

    def get_y(self): #Returns the y coordinate
        return self.__y
    
    def get_width(self): #Returns the width of the food
        return self.__width
    
    def get_height(self): #Returns the height of the food
        return self.__height
    
    def get_colour(self): #Returns the colour of the food
        return self.__colour
    
    def __str__(self): #Returns a string representation of the food's color and coordinates.
        return f"Food: Colour={self.__colour}, Coordinates=({self.__x}, {self.__y})"