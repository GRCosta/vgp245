import pygame

pygame.init()


# Basic settings for screen resolution
display_width = 1024
display_height = 800

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Trapped Mushroom")

# Changing the color of the back screen
white = pygame.Color(255, 255, 255, 255)
black = pygame.Color(0, 0, 0, 255)
blue = pygame.Color(0, 0, 255, 255)

x = 10
y = 10

# Main loop to keep the window alive
is_running = True

clock = pygame.time.Clock()

def text_object(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('Arial', 100)
    text_surf, text_rect = text_object(text, largeText)
    text_rect.center = (display_width * 0.5, display_height * 0.5)
    screen.blit(text_surf, text_rect)


class Sprite:
    """A sprite object"""
    x
    y
    radius = 1
    img = ""

    def __init__(self, x, y, radius, img):
        self.x = x
        self.y = y
        self.radius = radius
        self.img = pygame.image.load(img)

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))


def check_collision(player, obstacle):
    if(isinstance(player, Sprite) and isinstance(obstacle, Sprite)):
        raise ValueError("Type of object is not Sprite!!")
    
    distance = (player.x - obstacle.x)**2 + (player.y - obstacle.y)**2
    sq_sum_radius = (player.radius + obstacle.radius)**2

    if distance > sq_sum_radius:
        return False        # Not colliding

    else:
        return True         # Colliding


mario_sprite = Sprite(x, y, 32, 'mario_idle_01.png')
obst_obj = Sprite(200, 200, 16, 'mushroom.png')


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # Basic controls        
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        mario_sprite.y += 5
    elif pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        mario_sprite.y -= 5

    if pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
        mario_sprite.x += 5  
    elif pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]:
        mario_sprite.x -= 5  
            
    x = max(mario_sprite.x, 0)
    x = min(mario_sprite.x, display_width - (mario_sprite.radius * 2))
    y = max(mario_sprite.y, 0)
    y = min(mario_sprite.y, display_height - (mario_sprite.radius * 2))
    
if(check_collision(mario_sprite, obst_obj)):
    


    
    screen.fill(white)
    mario_sprite.render(screen)
    obst_obj.render(screen)

    message_display("Trapped Mushroom")

    pygame.display.flip()

    clock.tick(60)

    

pygame.quit()
quit()