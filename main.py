#import pygame library and classes
import pygame
from pacman import Pacman
from enemy import Enemy
from food import Food

#initialise pygame
pygame.init()

# --- SETUP
#setup characteristics of the drawable components
#creating a display window
#DISPLAY_SIZE --> gives the width of the display
DISPLAY_SIZE = [600, 600]
display = pygame.display.set_mode(DISPLAY_SIZE)
dark_grey = [50, 50, 50] #[red, green, blue]

#characteristics of the pacman object
pacman_x = DISPLAY_SIZE[0] // 2
pacman_y = 40
pacman_radius = 20
pacman_colour = [255, 255, 0]
#instance of the pacman class is created
pacman = Pacman(pacman_x, pacman_y, pacman_radius, pacman_colour, 3)

#characteristics of the enemy object
enemy_x = 550
enemy_y = 450
enemy_radius = 10
enemy_colour = [255, 0, 0]
#instance of the enemy class is created
enemy = Enemy(enemy_x, enemy_y, enemy_colour, enemy_radius, 1, 1)

#characteristics of the food object
food_x = DISPLAY_SIZE[0] // 4
food_y = 70
food = Food(food_x, food_y)

#initialise Clock (amount of times per second the screen refreshes)
clock = pygame.time.Clock()

#initialise font for the string representations
font = pygame.font.SysFont(None, 24)

#initialise scores
pacman_score = 0
enemy_score = 0

#run_game = True
run_game = True

#Boolean assignments to control the movement of pacman
down_pressed = False
up_pressed = False
right_pressed = False
left_pressed = False

# --- Game loop
#Within this loop, the program listens for events and resonds to them. --> Event Driven Programming
while run_game:
# ---- draw display window
    display.fill(dark_grey)
# ---- prepare drawable elements(
    pacman.draw(display)
    enemy.draw(display)
    food.draw(display)
 
# ---- listen to events and respond:
    #Check for collisions between the enemy and the pacman
    #When both edges of each shape collide, they are relocated to random locations within the game display using the relocate methods
    if (enemy.get_x() + enemy.get_radius() > pacman.get_x() - pacman.get_radius() and 
        enemy.get_x() - enemy.get_radius() < pacman.get_x() + pacman.get_radius() and 
        enemy.get_y() + enemy.get_radius() > pacman.get_y() - pacman.get_radius() and 
        enemy.get_y() - enemy.get_radius() < pacman.get_y() + pacman.get_radius()):
        enemy.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
        pacman.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))

    #Check for collisions between the enemy and the food
    #When both edges of each shape collide, they are relocated to random locations within the game display using the relocate methods contained in their classes
    if (enemy.get_x() + enemy.get_radius() > food.get_x() and 
        enemy.get_x() - enemy.get_radius() < food.get_x() + food.get_width() and 
        enemy.get_y() + enemy.get_radius() > food.get_y() and 
        enemy.get_y() - enemy.get_radius() < food.get_y() + food.get_height()):
        enemy.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
        food.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
        food_x = food.get_x()  #Update food_x with new coordinates to ensure the enemy keeps chasing the new food location
        food_y = food.get_y()  #Update food_y with new coordinates to ensure the enemy keeps chasing the new food location
        enemy_score += 1 #Enemys score is incremented every time it eats the food

    #Check for collisions between the pacman and the food
    #When both edges of each shape collide, they are relocated to random locations within the game display using the relocate methods contained in their classes
    if (pacman.get_x() + pacman.get_radius() > food.get_x() and 
        pacman.get_x() - pacman.get_radius() < food.get_x() + food.get_width() and 
        pacman.get_y() + pacman.get_radius() > food.get_y() and 
        pacman.get_y() - pacman.get_radius() < food.get_y() + food.get_height()):
        pacman.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
        food.relocate(DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
        food_x = food.get_x()  # Update food_x with new coordinates to ensure the enemy keeps chasing the new food location
        food_y = food.get_y()  # Update food_y with new coordinates to ensure the enemy keeps chasing the new food location
        pacman_score += 1 #Pacman's score is incremented every time it eats the food

    #Moves enemy towards the centre of the food
    if enemy.get_x() < food_x + (food.get_width()/2):
        enemy.move("RIGHT", DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
    else:
        enemy.move("LEFT", DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
    if enemy.get_y() < food_y + (food.get_height()/2):
        enemy.move("DOWN", DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))
    else:
        enemy.move("UP", DISPLAY_SIZE[0], (DISPLAY_SIZE[1] - 100))

    #Moving pacman based on key presses and the Boolean assignments
    if down_pressed == True and right_pressed == False and left_pressed == False:
        pacman.move_down()
    if up_pressed == True and right_pressed == False and left_pressed == False:
        pacman.move_up()
    if right_pressed == True and up_pressed == False and down_pressed == False:
        pacman.move_right()
    if left_pressed == True and up_pressed == False and down_pressed == False: 
        pacman.move_left()

    #String representations are created and displayed below the game. 
    #Pacman string representaion is the same colour as the pacman object
    pacman_text = font.render(str(pacman), True, pacman.get_colour())
    display.blit(pacman_text, (10, DISPLAY_SIZE[1] - 80))
    
    #Enemy string representaion is the same colour as the Enemy object
    enemy_text = font.render(str(enemy), True, enemy.get_colour())
    display.blit(enemy_text, (10, DISPLAY_SIZE[1] - 55))
    
    #Food string representaion is the same colour as the Food object
    food_text = font.render(str(food), True, food.get_colour())
    display.blit(food_text, (10, DISPLAY_SIZE[1] - 30))
    
    #Scoreboards for Pacman and the Enemy are displayed alongside the string representations
    pacman_score_text = font.render(f"Pacman: {pacman_score}", True, pacman.get_colour())
    display.blit(pacman_score_text, (DISPLAY_SIZE[0] - 100, DISPLAY_SIZE[1] - 80)) 
    enemy_score_text = font.render(f"Enemy: {enemy_score}", True, enemy.get_colour())
    display.blit(enemy_score_text, (DISPLAY_SIZE[0] - 100, DISPLAY_SIZE[1] - 55)) 
        
# -------- listen out to mouse keyboard etc events and when application is quit
    '''
    A list of every event that takes place is returned by this function. 
    The program iterates through this list, resoonding to every event.
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
            if event.key == pygame.K_RIGHT:
                right_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False

# -------- if application is quit --> run_game = False (break out of game loop)
        if event.type == pygame.QUIT:
            run_game = False

# ---- update the display window (prepared drawable elements will not appear without this!)
    pygame.display.update()
# ---- update the Clock (framerate)
    clock.tick(60)
	
# ---- when game loop terminates
# ---- deinitialise pygame
pygame.quit()
# ---- quit application
quit()
