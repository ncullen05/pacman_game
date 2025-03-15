import pygame, random

'''
The Enemy class is designed to represent the Enemy character in the game.
It includes methods to draw the Enemy on the screen, move the Enemy in towards the food, and relocate the Enemy to a random position. 
A reset speed method ensures that the Enemy does not stop moving once it eats the food once.
There are also a series of getters to access private instance variables such as the 'x' and 'y' coordinates, radius, and colour
The class also includes a string representation method to display the Enemy's colour and coordinates.
'''

class Enemy:

    def __init__(self, x, y, colour, radius, speed_x, speed_y): #Initialises the Enemy object
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__colour = colour
        self.__speed_x, self.__speed_y = speed_x, speed_y
    
    def draw(self, display): #Draws the Enemy on the screen
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius)

    def move(self, direction, display_width, display_height): #Moves the Enemy in accordance with inputted string and ensures it never leaves the frame
        if direction == "RIGHT":
            self.__x += self.__speed_x
        elif direction == "LEFT":
            self.__x -= self.__speed_x
        elif direction == "DOWN":
            self.__y += self.__speed_y
        elif direction == "UP":
            self.__y -= self.__speed_y

        if self.__x < 0:
            self.__x = 0
        elif self.__x > display_width - self.__radius:
            self.__x = display_width - self.__radius

        if self.__y < 0:
            self.__y = 0
        elif self.__y > (display_height - 100) - self.__radius:
            self.__y = (display_height - 100) - self.__radius

    def get_x(self): #Returns the x coordinate
        return self.__x

    def get_y(self): #Returns the y coordinate
        return self.__y
    
    def get_radius(self): #Returns the radius of the Enemy
        return self.__radius
    
    def get_colour(self): #Returns the colour of the Enemy
        return self.__colour
    
    def reset_speed(self, speed_x, speed_y): #Resets the speed of the Enemy so they do not come to a stand still
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def relocate(self, display_width, display_height): #Relocates the Enemy to a random position within the display boundaries.
        self.__x = random.randint(0, display_width - self.__radius)
        self.__y = random.randint(0, (display_height - 100) - self.__radius)
        self.reset_speed(1, 1) 

    def __str__(self): #Returns a string representation of the Enemy's color and coordinates.
        return f"Enemy: Colour={self.__colour}, Coordinates=({self.__x}, {self.__y})"