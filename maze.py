#Persiapan File dan Aset-aset
from pygame import*
window = display.set_mode((700, 500))

display.set_caption("Labirin")
bg = image.load("background.jpg")
bg = transform.scale(bg, (700, 500))

mixer.init()
mixer.music.load('bintang5.ogg')
mixer.music.play()
mixer.music.set_volume(0.1) 

#Resep untuk membuat karakter
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
        if keys [K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 500 - 80 :
            self.rect.y += self.speed

class Enemy (GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__(player_image, player_x, player_y, player_speed)
        self.arah = 'right'
    def update(self):
        if self.arah == 'right':
            self.rect.x += self.speed
        if self.arah == 'left':
            self.rect.x -= self.speed
        
        if self.rect.x < 470:
            self.arah = 'right'
        if self.rect.x > 615:
            self.arah = 'left'
class Wall(sprite.Sprite):
    def __init__(self, c1, c2, c3, x, y, w, h):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill((c1, c2, c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(24, 46, 217, 100 , 20, 450, 10)
w2 = Wall(24, 46, 217, 100, 480, 350, 10)
w3 = Wall(24, 46, 217, 100, 20, 10, 380)
w4 = Wall(24, 46, 217, 200, 130, 10, 350)
w5 = Wall(24, 46, 217, 450, 130, 10, 360)
w6 = Wall(24, 46, 217, 300, 20, 10, 350)
w7 = Wall(24, 46, 217, 390, 120, 130, 10)

packman = Player('hero.png', 30, 200, 5)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)
clock = time.Clock()
fps = 60

font.init()
font = font. Font (None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (235, 5, 28))

# Loop Game
finish = False
run = True
while run:
    clock.tick(fps)
    # Mendeteksi Event
    for e in event.get():
        if e.type == QUIT:
            run = False
    # Meletakkan Aset dan Objek
    if finish == False:
        window.blit(bg, (0, 0))
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        monster.reset()
        packman.reset()
        final.reset()
        packman.update()
        monster.update()
    
    if sprite.collide_rect(packman, w1):
        finish = True
        window.blit(lose, (50, 50))

    if sprite.collide_rect(packman, w2):
        finish = True
        window.blit(lose, (50, 50))

    if sprite.collide_rect(packman, w3):
        finish = True
        window.blit(lose, (50, 50))
    
    if sprite.collide_rect(packman, w4):
        finish = True
        window.blit(lose, (50, 50))
    
    if sprite.collide_rect(packman, w5):
        finish = True
        window.blit(lose, (50, 50))

    if sprite.collide_rect(packman, w6):
        finish = True
        window.blit(lose, (50, 50))   

    if sprite.collide_rect(packman, w7):
        finish = True
        window.blit(lose, (50, 50)) 

    if sprite.collide_rect(packman, monster):
        finish = True
        window.blit(lose, (50, 50))

    if sprite.collide_rect(packman, final):
        finish = True
        window.blit(win, (50, 50))
    
    
    display.update()
