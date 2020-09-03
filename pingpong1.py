import pygame

pygame.init()

win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong')

white = (255, 255, 255)
black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.points = 0
        
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        

paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
paddle1.rect.x = 25
paddle1.rect.y = 250
paddle2.rect.x = 715
paddle2.rect.y = 250
ball.rect.x = 375
ball.rect.y = 250


all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

def redraw():
    win.fill(black)
    all_sprites.draw(win)
    pygame.display.update()

run = True

while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw()

pygame.quit()