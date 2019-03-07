import pygame


WIDTH = 640
HEIGHT = 480
FPS = 30

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


counter = 0


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, size, mass, velocity, color):
        self.mass = mass
        self.velocity = velocity
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

    def update(self):
        self.rect.x += self.velocity


# initialisers
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Collision Demo")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

# group all the sprites together to make updating the game easier
all_sprites = pygame.sprite.Group()
square1 = Square(300, HEIGHT, 50, 1, 0, GREEN)
square2 = Square(400, HEIGHT, 100, 100, -1, BLUE)
wall = Square(-2000, HEIGHT, 2000, 0, 0, BLACK)
all_sprites.add(square1)
all_sprites.add(square2)


def is_wall(square):
    return square.mass == 0


def do_collision(body1, body2):
    x_initial_velocity = body1.velocity
    y_initial_velocity = body2.velocity
    body1.velocity = ((float(body1.mass - body2.mass) / float(body1.mass + body2.mass)) * x_initial_velocity) + (
                (float(2 * body2.mass) / float(body1.mass + body2.mass)) * y_initial_velocity)
    body2.velocity = ((float(2 * body1.mass) / float(body1.mass + body2.mass)) * x_initial_velocity) + (
                (float(body2.mass - body1.mass) / float(body1.mass + body2.mass)) * y_initial_velocity)


# TO FINISH
def check_collisions(*args):
    bodies = args
    global counter

    for x in range(len(bodies)):
        # SQUARES COLLISION
        for y in range(x + 1, len(bodies)):
            # LEFT
            if bodies[x].rect.bottomleft[0] + bodies[x].velocity <= bodies[y].rect.bottomright[0] and \
                    bodies[y].rect.bottomleft[0] <= bodies[x].rect.bottomleft[0] + bodies[x].velocity:
                while bodies[x].rect.bottomleft >= bodies[y].rect.bottomright:
                    bodies[x].rect.bottomleft = (bodies[x].rect.bottomleft[0] - 1, HEIGHT)
                if is_wall(bodies[y]):
                    bodies[x].velocity *= -1

                    counter = counter + 1
                    print(counter)

                    print(bodies[x].velocity)

                    break
                else:
                    do_collision(bodies[x], bodies[y])

                    counter = counter + 1
                    print(bodies[y].velocity)
                    print(bodies[x].velocity)
                    break
            
            # RIGHT
            if bodies[x].rect.bottomright[0] + bodies[x].velocity >= bodies[y].rect.bottomleft[0] and \
                    bodies[y].rect.bottomright[0] >= bodies[x].rect.bottomright[0] + bodies[x].velocity:
                while bodies[x].rect.bottomright <= bodies[y].rect.bottomleft:
                    bodies[x].rect.bottomleft = (bodies[x].rect.bottomleft[0] + 1, HEIGHT)
                if is_wall(bodies[y]):
                    bodies[x].velocity *= -1

                    counter = counter + 1
                    break
                else:
                    do_collision(bodies[x], bodies[y])

                    counter = counter + 1
                    print(counter)
                    print(bodies[y].velocity)
                    print(bodies[x].velocity)
                    break


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE) #creates surface for python to render pixels onto to write text, true is for pixellation (aliasing)
    text_rect = text_surface.get_rect() #figures out the rectangle size and shape fo the surface
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect) #takes the text surface and blits it onto the screen


# Game Loop
running = True
while running:
    # keep loop running at right time
    clock.tick(FPS)
    # Process inputs
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

    check_collisions(square1, square2, wall)

    # Update
    all_sprites.update()

    # Draw events
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, "Collisions: " + str(counter), 36, 500, 30)
    # Flip comes after drawing everything
    pygame.display.flip()

pygame.quit()
