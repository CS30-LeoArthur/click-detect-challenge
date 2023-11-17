import pygame
import random
# Define Colors
GREY = (128, 128, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
circle_list = []
rectangle_list = []

def mouse_position():
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    return [mouse_x, mouse_y]

def rectCollide(rect1, rect2):
    return rect1.x < rect2.x + rect2.width and rect1.y < rect2.y + rect2.height and rect1.x + rect1.width > rect2.x and rect1.y + rect1.height > rect2.y

class Circle():
    def __init__(self, x, y, width, height, x_change, y_change):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_change = x_change
        self.y_change = y_change
    
    def draw_circle(self, screen):
        pygame.draw.ellipse(screen, GREEN, [self.x, self.y, self.width, self.height], 2)
    
    def circle_update(self):
        self.x = self.x + self.x_change
        self.y = self.y + self.y_change

    def edge_collision(self):
        if self.x > SCREEN_WIDTH - self.width:
            self.x_change = -5
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y_change = -5
        elif self.x < 0:
            self.x_change = 5
        elif self.y < 0:
            self.y_change = 5

circle_list.append(Circle(random.randrange(10, 700), random.randrange(10, 700), random.randrange(50, 100), random.randrange(50, 100), 5, 5))
circle_list.append(Circle(random.randrange(10, 700), random.randrange(10, 700), random.randrange(50, 100), random.randrange(50, 100), 5, 5))
circle_list.append(Circle(random.randrange(10, 700), random.randrange(10, 700), random.randrange(50, 100), random.randrange(50, 100), 5, 5))
circle_list.append(Circle(random.randrange(10, 700), random.randrange(10, 700), random.randrange(50, 100), random.randrange(50, 100), 5, 5))
circle_list.append(Circle(random.randrange(10, 700), random.randrange(10, 700), random.randrange(50, 100), random.randrange(50, 100), 5, 5))

class Rectangle():
    def __init__(self, x, y, width, height, x_change, y_change):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_change = x_change
        self.y_change = y_change
    
    def draw_rectangle(self, screen):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.width, self.height,])



def main():
    # Initialize pygame
    pygame.init()

    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode((size))

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Loop until the user clicks the close button
    done = False
    # Main Program Loop
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Logic stuff
        for i in range (len(circle_list)):
            circle_list[i].edge_collision()
        
        for i in range(len(circle_list)):
            circle_list[i].circle_update()

        # Drawing stuff
        # Clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command. 
        screen.fill(BLACK) 
        for i in range(len(circle_list)):
            circle_list[i].draw_circle(screen) 

        # Update screen with what is drawn
        pygame.display.flip()

        # Limit to 60 fps
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()