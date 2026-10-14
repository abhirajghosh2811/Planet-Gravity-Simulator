import pygame
import sys
import numpy as np

pygame.init()

#User inputs
velocities = np.array([3.7, 8.87, 9.81, 3.71, 24.79, 10.44, 8.69, 11.15, 274.0])
planets = np.array(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Sun"])

for i in range(9):
    print(f"{i+1}. {planets[i]} : ",velocities[i]) #For user friendliness..I know the terminal itself isn't user friendly
while True:
    try:
        print("Pass in a number from 1 to 9")
        usernum = int(input("Choose a number for the desired velocity : ")) 
        if usernum < 1 or usernum > 9:
            print("Stupid")
            continue
        userchoice = velocities[usernum-1] #Same as the last one, for user friendliness
        break

    except ValueError:
        print("Pass in a correct value, stupid.") #To roast the user

#Variables
screenwidth = 800
screenheight = 500
fps = 60

#Numpy arrays
circleV = np.array([5, 20], 'int32')
circlepos = np.array([400, 100], 'int32')
gravity = 0
velocity = 0.45
floor = screenheight - 50

#Colors
black = (0, 0, 0)
white = (255, 255, 255)

#Classes
class circle:
    def __init__(self, screen, color, position, radius, border, gravity, velocity):
        self.screen = screen
        self.color = color
        self.position = position
        self.radius = radius
        self.border = border
        self.gravity = gravity
        self.velocity = velocity

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, self.border)

    def fall(self):
        self.gravity += self.velocity
        self.position[1] += self.gravity

        if self.position[1] >= floor:
            self.position[1] = floor
            self.gravity = -self.gravity * 0.8
            if abs(self.gravity) < 1:
                self.gravity = 0
                self.velocity = 0

#Pygame screen
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()

#Instances
maincircle = circle(screen, white, circlepos, circleV[1], circleV[0], gravity, userchoice)

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Keybindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #Fill screen
    screen.fill(black)

    #Circle
    maincircle.fall()
    maincircle.draw()

    clock.tick(fps)
    pygame.display.update()
