from pygame import *

mixer.init()
mixer.music.load('serce.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)

window = display.set_mode((700,500))
display.set_caption("пинг-понг")
background = transform.scale(image.load('fon.jpg'), (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -80:
           self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height -80:
           self.rect.y += self.speed

win_width = 700
win_height = 500
game = True
finish = False

player1 = Player('racket.png', 1, win_height-100, 35, 95, 7)
player2 = Player('racket.png', 665, win_height-100, 35, 95, 7)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))

    player1.update1()
    player2.update2()
    player1.reset()
    player2.reset()

    display.update()
    time.delay(20)