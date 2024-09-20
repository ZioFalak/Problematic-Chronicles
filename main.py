import pygame, sys
from settings import *
from tile import Tile
from pygame.locals import *
import random

        # general setup
pygame.init()
pygame.display.set_caption("Problematic Chronicles")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
clock = pygame.time.Clock()
font = pygame.font.SysFont('cambria',30)

def text(text, font, colour, surface, x, y):
    text_obj = font.render(text, True , colour)
    textrect = text_obj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text_obj, textrect)
    
shoot_sfx = pygame.mixer.Sound('music/gunshotsfx.mp3')
songs = ["music/LetItFly.mp3", "music/Drowning.mp3", "music/creepin.mp3"]
current_song_index = 0

# Load the first song in the songs
pygame.mixer.music.load(songs[current_song_index])

# Set volume for songs and sfx
music_volume = 1
sfx_volume = 1

# Set the end event for when the current song finishes playing
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Start playing the current song
pygame.mixer.music.play()

def mainMenu():
    global screen
    global songs
    global current_song_index
    global SONG_END
    click = False
    fullscreen = False
        # images
    title = pygame.image.load("mainPictures/menuTitle2.png").convert_alpha()
    title.set_colorkey((0, 0, 0))    
    bg_width = 2000
    bg = pygame.image.load("mainPictures/mainbg.png").convert_alpha()
    bg = pygame.transform.scale(bg, (bg_width, screen.get_height()))
    i = 0

    while True:
        screen.fill('black')
        screen.blit(bg, (i,0))
        screen.blit(bg,(bg_width + i, 0))
        
        if i == - bg_width:
            screen.blit(bg,(bg_width + i, 0))
            i = 0
        i -= 0.5

        pos_x = (screen.get_width() - title.get_width())//2
        screen.blit(title, (pos_x,40))
        
        mx, my = pygame.mouse.get_pos()
            # Buttons
        button1 = pygame.image.load("mainPictures/START.png").convert_alpha()
        button1_rect = button1.get_rect(center = [screen.get_width()/2, 325])
        button1.set_colorkey((0, 0, 0))
        button2 = pygame.image.load("mainPictures/OPTIONS.png").convert_alpha()
        button2_rect = button2.get_rect(center = [screen.get_width()/2, 400])
        button2.set_colorkey((0, 0, 0))
        button3 = pygame.image.load("mainPictures/ABOUT.png").convert_alpha()
        button3_rect = button3.get_rect(center = [screen.get_width()/2, 475])
        button3.set_colorkey((0, 0, 0))
        button4 = pygame.image.load("mainPictures/EXIT.png").convert_alpha()
        button4_rect = button4.get_rect(center = [screen.get_width()/2, 550])
        button4.set_colorkey((0, 0, 0))
        
        if button1_rect.collidepoint((mx, my)):
            button1 = pygame.image.load("mainPictures/START_OUT.png").convert_alpha()
            button1_rect = button1.get_rect(center = [screen.get_width()/2, 325])
            button1.set_colorkey((0, 0, 0))
            if click == True:
                game()
        if button2_rect.collidepoint((mx, my)):
            button2 = pygame.image.load("mainPictures/OPTIONS_OUT.png").convert_alpha()
            button2_rect = button2.get_rect(center = [screen.get_width()/2, 400])
            button2.set_colorkey((0, 0, 0))
            if click == True:
                options()
        if button3_rect.collidepoint((mx, my)):
            button3 = pygame.image.load("mainPictures/ABOUT_OUT.png").convert_alpha()
            button3_rect = button3.get_rect(center = [screen.get_width()/2, 475])
            button3.set_colorkey((0, 0, 0))
            if click == True:
                about()

        if button4_rect.collidepoint((mx, my)):
            button4 = pygame.image.load("mainPictures/EXIT_OUT.png").convert_alpha()
            button4_rect = button4.get_rect(center = [screen.get_width()/2, 550])
            button4.set_colorkey((0, 0, 0))
            if click == True:
                pygame.quit()
                sys.exit()
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT))
            if event.type == SONG_END: # the current song has finished playing
                    current_song_index = (current_song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()

        bg = pygame.transform.scale(bg, (2000, screen.get_height()))
        screen.blit(button1, button1_rect)
        screen.blit(button2, button2_rect)
        screen.blit(button3, button3_rect)
        screen.blit(button4, button4_rect)

        pygame.display.update()
        clock.tick(FPS)

def options():
    global screen
    global songs
    global current_song_index
    global SONG_END
    global music_volume
    global sfx_volume
    global shoot_sfx
    running = True
    click = False
        # buttons to change volume
    music_button = pygame.Surface((60,52))
    music_button.set_alpha(40)
    mbutton_rect = music_button.get_rect(topleft = ((screen.get_width()//2) + 180, (screen.get_height()//2) - 13))
    music_button2 = pygame.Surface((60,52))
    music_button2.set_alpha(0)
    mbutton2_rect = music_button2.get_rect(topleft = ((screen.get_width()//2) + 292, (screen.get_height()//2) - 13))
    sfx_button = pygame.Surface((60,52))
    sfx_button.set_alpha(0)
    sbutton_rect = sfx_button.get_rect(topleft = ((screen.get_width()//2) + 180, (screen.get_height()//2) + 119))
    sfx_button2 = pygame.Surface((60,52))
    sfx_button2.set_alpha(0)
    sbutton2_rect = sfx_button2.get_rect(topleft = ((screen.get_width()//2) + 292, (screen.get_height()//2) + 119))

    dark_border = pygame.image.load('mainPictures/go_border.png').convert_alpha()
    dark_border = pygame.transform.scale(dark_border, (screen.get_width(), screen.get_height()))
    db_rect = dark_border.get_rect()
    book = pygame.image.load('mainPictures/optionpage.png').convert_alpha()
    book = pygame.transform.scale(book, (1051, 528))
    book_rect = book.get_rect(center = (screen.get_width()//2, screen.get_height()//2))
    time1 = 50
    
    while running:
        pygame.mixer.music.set_volume(music_volume)
        shoot_sfx.set_volume(sfx_volume)
        music_volume_bar2 = pygame.Rect((screen.get_width()//2) + 112, (screen.get_height()//2) - 41, music_volume * 300, 15)
        sfx_volume_bar2 = pygame.Rect((screen.get_width()//2) + 112, (screen.get_height()//2) + 91, sfx_volume * 300, 15)
        music_volume_bar = pygame.Rect((screen.get_width()//2) + 116, (screen.get_height()//2) - 45, music_volume * 300, 15)
        sfx_volume_bar = pygame.Rect((screen.get_width()//2) + 116, (screen.get_height()//2) + 87, sfx_volume * 300, 15)

        mx, my =  pygame.mouse.get_pos()

        dark_border.set_alpha(15)
        book.set_alpha(40)
        screen.blit(dark_border, db_rect)
        time1 -= 1
        if time1 <= 0:
            screen.blit(book, book_rect)
            pygame.draw.rect(screen, ('black'), music_volume_bar2)
            pygame.draw.rect(screen, ('black'), sfx_volume_bar2)
            pygame.draw.rect(screen, (230,230,230), music_volume_bar)
            pygame.draw.rect(screen, (230,230,230), sfx_volume_bar)
            time1 = 0
        
        if mbutton_rect.collidepoint(mx, my):
            if click:
                if music_volume > 0.1:
                    music_volume -= 0.1
                    
        if mbutton2_rect.collidepoint(mx, my):
            if click:
                if music_volume < 1:
                    music_volume += 0.1
                    
        if sbutton_rect.collidepoint(mx, my):
            if click:
                if sfx_volume > 0.1:
                    sfx_volume -= 0.1
                    
        if sbutton2_rect.collidepoint(mx, my):
            if click:
                if sfx_volume < 1:
                    sfx_volume += 0.1

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END: # the current song has finished playing
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # go to previous song
                    current_song_index = (current_song_index - 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_RIGHT: # go to next song
                    current_song_index = (current_song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(FPS)

def about():
    global screen
    global songs
    global current_song_index
    global SONG_END
    running = True

        # images
    dark_border = pygame.image.load('mainPictures/go_border.png').convert_alpha()
    dark_border = pygame.transform.scale(dark_border, (screen.get_width(), screen.get_height()))
    db_rect = dark_border.get_rect()
    book = pygame.image.load('mainPictures/aboutpage.png').convert_alpha()
    book = pygame.transform.scale(book, (1051, 528))
    book_rect = book.get_rect(center = (screen.get_width()//2, screen.get_height()//2))
    time1 = 50
    
    while running:
        dark_border.set_alpha(5)
        book.set_alpha(40)
        screen.blit(dark_border, db_rect)
        time1 -= 1
        if time1 <= 0:
            screen.blit(book, book_rect)
            time1 = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END: # the current song has finished playing
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(FPS)

def pause():
    global screen
    global songs
    global current_song_index
    global SONG_END
    running = True
    click = False

        # images
    dark_border = pygame.image.load('mainPictures/go_border.png').convert_alpha()
    dark_border = pygame.transform.scale(dark_border, (screen.get_width(), screen.get_height()))
    db_rect = dark_border.get_rect()
    paused = pygame.image.load("mainPictures/paused.png").convert_alpha()
    while running:
        pos_x = (screen.get_width() - paused.get_width())//2
        
        dark_border.set_alpha(80)
        screen.blit(dark_border, db_rect)

        mx, my = pygame.mouse.get_pos()
            # buttons
        button1 = pygame.image.load("mainPictures/START.png").convert_alpha()
        button1_rect = button1.get_rect(center = [screen.get_width()/2, 400])
        button1.set_colorkey((0, 0, 0))
        button2 = pygame.image.load("mainPictures/OPTIONS.png").convert_alpha()
        button2_rect = button2.get_rect(center = [screen.get_width()/2, 475])
        button2.set_colorkey((0, 0, 0))

        if button1_rect.collidepoint((mx, my)):
            button1 = pygame.image.load("mainPictures/START_OUT.png").convert_alpha()
            button1_rect = button1.get_rect(center = [screen.get_width()/2, 400])
            button1.set_colorkey((0, 0, 0))
            if click == True:
                running = False
        if button2_rect.collidepoint((mx, my)):
            button2 = pygame.image.load("mainPictures/OPTIONS_OUT.png").convert_alpha()
            button2_rect = button2.get_rect(center = [screen.get_width()/2, 475])
            button2.set_colorkey((0, 0, 0))
            if click == True:
                options()

        click = False        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == SONG_END: # the current song has finished playing
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(paused, (pos_x, (screen.get_height()//2) - paused.get_height()))
        screen.blit(button1, button1_rect)
        screen.blit(button2, button2_rect)
        pygame.display.update()
        clock.tick(FPS)

def game():
    global player
    global attack
    global attack_up
    global screen
    global songs
    global current_song_index
    global SONG_END
    global shoot_sfx
    global boss
    global boss_spawn
    global add_bullets
    global reduce_health
    
    fullscreen = False
    running = True
    add_bullets = 0
    reduce_health = 0
    bg_colour = (115, 199, 161)
    bg_colour = (62, 148, 108)
        # IMAGES
    bg = pygame.image.load('mainPictures/bg.png').convert_alpha()
    tree = pygame.image.load("mainSprites/tree4.png").convert_alpha()
    tree = pygame.transform.scale(tree, (64,73))
    tree.set_colorkey("black")
    cloak = pygame.image.load('mainSprites/cloak.png').convert_alpha()
    dead_tree = pygame.image.load("mainSprites/treed.png").convert_alpha()
    dead_tree = pygame.transform.scale(dead_tree, (64, 73))
    key = pygame.image.load('mainSprites/key.png').convert_alpha()
    key = pygame.transform.scale(key, (39, 53))
    water = pygame.image.load('mainSprites/water.png').convert_alpha()
    water_bottomL = pygame.image.load('mainSprites/waterc.png').convert_alpha()
    water_bottomR = pygame.image.load('mainSprites/waterc2.png').convert_alpha()
    water_down = pygame.image.load('mainSprites/waterdown.png').convert_alpha()
    water_right = pygame.image.load('mainSprites/waterright.png').convert_alpha()
    water_left = pygame.image.load('mainSprites/waterleft.png').convert_alpha()
    water_up = pygame.image.load('mainSprites/waterup.png').convert_alpha()
    water_topright = pygame.image.load('mainSprites/waterright2.png').convert_alpha()
    water_topleft = pygame.image.load('mainSprites/waterleft2.png').convert_alpha()
    water_topright2 = pygame.image.load('mainSprites/waterleft3.png').convert_alpha()
    skull_health = pygame.image.load('mainSprites/bossHealth.png'). convert_alpha()
    attack_up = pygame.image.load('mainPictures/attackUp.png').convert_alpha()
    ammo = pygame.image.load("mainSprites/bullet.png").convert_alpha()
    
    class Player(pygame.sprite.Sprite):
        def __init__(self, pos, groups, obstacles):    
            super().__init__(groups)

            charUp = pygame.image.load("mainSprites/mainright.png")
            charUp = pygame.transform.scale(charUp, (48,48))
            charUp.set_colorkey((237, 28, 36))
            
            self.image = charUp.convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
            self.direction = pygame.math.Vector2()
            self.True_direction = 'right'
            self.speed = 7
            
            self.max_health = 100
            self.health = 100
            self.alive = True
            self.max_ammo = 100
            self.ammo = 100
            self.damage = 25
            self.attack_up = 0
            self.key = False
            self.kills = 0

            self.obstacles = obstacles

        def input(self, image):
            w = 48
            h = 48
            
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_w]:
                self.True_direction = 'up'
                self.direction.y = -1
                charUp = pygame.image.load("mainSprites/mainup.png")
                charUp = pygame.transform.scale(charUp, (w,h))
                charUp.set_colorkey((237, 28, 36))
                self.image = charUp
            elif keys[pygame.K_s]:
                self.True_direction = 'down'
                self.direction.y = 1
                charDown = pygame.image.load("mainSprites/maindown.png")
                charDown = pygame.transform.scale(charDown, (w,h))
                charDown.set_colorkey((237, 28, 36))
                self.image = charDown
            else:
                self.direction.y = 0
                self.image = self.image
            if keys[pygame.K_a]:
                self.True_direction = 'left'
                self.direction.x = -1
                charLeft = pygame.image.load("mainSprites/mainleft.png")
                charLeft = pygame.transform.scale(charLeft,(w,h))
                charLeft.set_colorkey((237, 28, 36))
                self.image = charLeft
            elif keys[pygame.K_d]:
                self.True_direction = 'right'
                self.direction.x = 1
                charRight = pygame.image.load("mainSprites/mainright.png")
                charRight = pygame.transform.scale(charRight, (w,h))
                charRight.set_colorkey((237, 28, 36))
                self.image = charRight
            else:
                self.direction.x = 0
                self.image = self.image

        def move(self, speed):
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical')
        
        def collision(self,direction):
            if direction == 'horizontal':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
            
            if direction == 'vertical':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom

        def create_bullet(self):
            bullet = pygame.image.load("mainSprites/bullet.png").convert_alpha()
            return Bullet(self.rect.x, self.rect.y, self.True_direction, bullet)

        def update(self):
            self.input(self.image)
            self.move(self.speed)

            if self.health <= 0:
                self.alive = False

            for enemies in enemy_group:
                if pygame.sprite.collide_rect(self, enemies):
                    self.health -= 0.25
            if pygame.sprite.spritecollide(self, boss_group, False):
                self.health -= 0.75

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, posX, posY, direction, image):
            super().__init__()
            self.posX = posX + 24
            self.posY = posY + 24
            self.image = image.convert_alpha()
            self.rect = self.image.get_rect(center = (self.posX, self.posY))
            
            self.speed = 10
            self.direction = direction

        def update(self):
            if self.direction == 'up':
                self.rect.x += (0 * self.speed)
                self.rect.y += (-1 * self.speed)
            if self.direction == 'down':
                self.rect.x += (0 * self.speed)
                self.rect.y += (1 * self.speed)
            if self.direction == 'left':
                self.rect.x += (-1 * self.speed)
                self.rect.y += (0 * self.speed)
            if self.direction == 'right':
                self.rect.x += (1 * self.speed)
                self.rect.y += (0 * self.speed)

            for enemies in enemy_group:
                if pygame.sprite.spritecollide(enemies, bullet_group, False):
                    enemies.health -= player.damage
                    self.kill()
            if pygame.sprite.spritecollide(self, tile_group, False):
               self.kill()
            if pygame.sprite.spritecollide(self, boss_group, False):
                boss.health -= player.damage // 2
                self.kill()

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, pos, groups, obstacles):    
            super().__init__(groups)
            
            self.current_image = 0
            self.images = []
            self.images.append(pygame.image.load('mainSprites/enemy1.png').convert_alpha())
            self.images.append(pygame.image.load('mainSprites/enemy2.png').convert_alpha())
            self.image = self.images[self.current_image]
            self.rect = self.image.get_rect(topleft = pos)
            self.direction = pygame.math.Vector2()
            self.speed = 4

            self.max_health = 100
            self.health = 100
            self.alive = True

            self.obstacles = obstacles

        def move(self, speed, image):
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
            enemy_vec = pygame.math.Vector2(self.rect.center)
            player_vec = pygame.math.Vector2(player.rect.center)
            distance = (player_vec - enemy_vec).magnitude()
            if distance > 0:
                self.direction = (player_vec - enemy_vec).normalize()
            else: 
                self.direction = pygame.math.Vector2()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical') 

        def collision(self,direction):
            if direction == 'horizontal':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
            
            if direction == 'vertical':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom

        def update(self):
            self.move(self.speed, self.image)
            self.image = self.images[int(self.current_image)]
            self.current_image += 0.05
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.image = self.images[int(self.current_image)]

            if self.health <= 0 :
                self.alive = False
                if player.attack_up != 10:
                    player.attack_up += 0.5
                    player.damage += 7.5/2
                    player.kills += 1
                self.kill()

    class Boss(pygame.sprite.Sprite):
        def __init__(self, pos, groups, obstacles):    
            super().__init__(groups)
            
            self.current_image = 0
            self.images_2 = []
            self.images_2.append(pygame.image.load('mainSprites/boss1.png').convert_alpha())
            self.images_2.append(pygame.image.load('mainSprites/boss2.png').convert_alpha())
            self.images_2.append(pygame.image.load('mainSprites/boss3.png').convert_alpha())
            self.images_2.append(pygame.image.load('mainSprites/boss4.png').convert_alpha())
            self.images = []
            self.images.append(pygame.image.load('mainSprites/mboss.png').convert_alpha())
            self.images.append(pygame.image.load('mainSprites/mboss2.png').convert_alpha())
            self.image = self.images[self.current_image]
            self.rect = self.image.get_rect(topleft = pos)
            self.direction = pygame.math.Vector2()
            self.speed = 3

            self.max_health = 800
            self.health = 800
            self.alive = True

            self.obstacles = obstacles

        def move(self, speed, image):
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
            enemy_vec = pygame.math.Vector2(self.rect.center)
            player_vec = pygame.math.Vector2(player.rect.center)
            distance = (player_vec - enemy_vec).magnitude()
            if distance > 0:
                self.direction = (player_vec - enemy_vec).normalize()
            else: 
                self.direction = pygame.math.Vector2()

            self.rect.x += self.direction.x * speed
            self.collision('horizontal')
            self.rect.y += self.direction.y * speed
            self.collision('vertical') 

        def collision(self,direction):
            if direction == 'horizontal':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
            
            if direction == 'vertical':
                for sprite in self.obstacles:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom

        def create_bullet(self, directions):
            bullet = pygame.image.load("mainSprites/fiball0.png")
            return boss_bullet(self.rect.x, self.rect.y, directions, bullet)

        def shoot(self):
            bullet_group.add(self.create_bullet('up'))
            bullet_group.add(self.create_bullet('down'))
            bullet_group.add(self.create_bullet('left'))
            bullet_group.add(self.create_bullet('right'))

        def update(self):
            self.move(self.speed, self.image)
            if self.health >= 401:
                self.image = self.images[int(self.current_image)]
                self.current_image += 0.05
                if self.current_image >= len(self.images):
                    self.current_image = 0
                self.image = self.images[int(self.current_image)]
            
            if self.health <= 400:
                self.speed = 5
                self.image = self.images_2[int(self.current_image)]
                self.current_image += 0.1
                if self.current_image >= len(self.images_2):
                    self.current_image = 0
                self.image = self.images_2[int(self.current_image)]
                    
            if self.health <= 0:
                self.alive = False
                player.health = player.max_health
                self.kill()

    class boss_bullet(pygame.sprite.Sprite):
        def __init__(self, posX, posY, direction, image):
            super().__init__()
            self.posX = posX + 40
            self.posY = posY + 50
            self.image = image.convert_alpha()
            self.rect = self.image.get_rect(center = (self.posX, self.posY))
            
            self.speed = 8
            self.direction = direction

        def update(self):
            if self.direction == 'up':
                self.rect.x += (0 * self.speed)
                self.rect.y += (-1 * self.speed)
            if self.direction == 'down':
                self.rect.x += (0 * self.speed)
                self.rect.y += (1 * self.speed)
            if self.direction == 'left':
                self.rect.x += (-1 * self.speed)
                self.rect.y += (0 * self.speed)
            if self.direction == 'right':
                self.rect.x += (1 * self.speed)
                self.rect.y += (0 * self.speed)

            if pygame.sprite.spritecollide(self, tile_group, False):
                self.kill()
        
            if pygame.sprite.spritecollide(self, player_group, False):
                player.health -= 15
                self.kill()

    class Camera(pygame.sprite.Group):
        def __init__(self):
            super().__init__()
            # camera offset
            self.surface = pygame.display.get_surface()
            self.mapWidth = self.surface.get_size()[0] // 2
            self.mapHeight = self.surface.get_size()[1] // 2
            self.offset = pygame.math.Vector2()

        def custDraw(self, player):
            if player.rect.centery >= self.mapHeight:
                self.offset.y = player.rect.centery - self.mapHeight
            else:
                self.offset.y = 0
            if player.rect.centerx >= self.mapWidth:
                self.offset.x = player.rect.centerx - self.mapWidth
            else:
                self.offset.x = 0

            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                offsetPos = sprite.rect.topleft - self.offset
                self.surface.blit(sprite.image, offsetPos)

            for enemies in enemy_group:
                health_rect = pygame.Rect((enemies.rect.x - self.offset.x) - 1, (enemies.rect.y - self.offset.y)- 10, enemies.health // 2, 5)
                health_border = pygame.Rect((enemies.rect.x -self.offset.x) - 3, (enemies.rect.y -self.offset.y) - 12, (enemies.max_health // 2) + 4, 9)
                pygame.draw.rect(screen, ('black'), health_border)
                pygame.draw.rect(screen, ('red'), health_rect)
            if boss.alive and boss_spawn:
                boss_border = pygame.Rect((screen.get_width()//2)- 405, (screen.get_height() - 90), boss.max_health + 10, 28)
                boss_health = pygame.Rect((screen.get_width()//2)- 400, (screen.get_height() - 86), boss.health, 20)
                pygame.draw.rect(screen, ('black'), boss_border)
                pygame.draw.rect(screen, ('red'), boss_health)
                screen.blit(skull_health, (screen.get_width()//2 - 435, (screen.get_height() - 110)))

    class bullet_camera(pygame.sprite.Group):
        def __init__(self):
            super().__init__()
            self.surface = pygame.display.get_surface()
            self.mapWidth = self.surface.get_size()[0] // 2
            self.mapHeight = self.surface.get_size()[1] // 2
            self.offset = pygame.math.Vector2()
                # background
            self.bg = bg
            self.bg_rect = self.bg.get_rect(topleft = (0,0))
            
        def custDraw(self, player):
            if player.rect.centery >= self.mapHeight:
                self.offset.y = player.rect.centery - self.mapHeight
            else:
                self.offset.y = 0
            if player.rect.centerx >= self.mapWidth:
                self.offset.x = player.rect.centerx - self.mapWidth
            else:
                self.offset.x = 0
            
            bg_offset = self.bg_rect.topleft - self.offset
            screen.blit(self.bg, bg_offset)

            for sprite in self.sprites():
                offsetPos = sprite.rect.topleft - self.offset
                self.surface.blit(sprite.image, offsetPos)
    
    class Block(pygame.sprite.Sprite):
        def __init__(self, pos, groups, image):
            super().__init__(groups)
            self.image = image
            self.rect = self.image.get_rect(topleft = pos)
            self.open = False
        
        def update(self):
            if player.key:
                obstacle_group.remove(self)

            if pygame.sprite.spritecollide(self, player_group, False):
                self.kill()

    class Key(pygame.sprite.Sprite):
        def __init__(self, pos, groups, image):
            super().__init__(groups)
            self.image = image
            self.rect = self.image.get_rect(topleft = pos)
        
        def update(self):
            if pygame.sprite.spritecollide(self, player_group, False):
                player.key = True
                print('collide', player.key)
                self.kill()


    visible_group = Camera()
    player_group = pygame.sprite.Group()
    bullet_group = bullet_camera()
    enemy_group = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()
    tile_group = pygame.sprite.Group()

        # Tile map
    for row_index, row in enumerate(map1):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 1:
                    Tile((x, y), [visible_group, tile_group, obstacle_group], tree)
                if col == 3:
                    Block((x + 17, y + 1), [visible_group, tile_group, obstacle_group], dead_tree)
                    Block((x - 20, y - 7), [visible_group, tile_group, obstacle_group], dead_tree)
                if col == 4:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water)
                if col == 5:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water_bottomL)
                if col == 6:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water_bottomR)
                if col == 7:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water_down)
                if col == 8:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water_right)
                if col == 9:
                    Tile((x, y +9), [visible_group, tile_group, obstacle_group], water_left)
                if col == 10:
                    Tile((x, y), [visible_group, tile_group, obstacle_group], water_up)
                if col == 11:
                    Tile((x, y), [visible_group, tile_group, obstacle_group], water_topright)
                if col == 12:
                    Tile((x, y), [visible_group, tile_group, obstacle_group], water_topleft)
                if col == 13:
                    Tile((x, y), [visible_group, tile_group, obstacle_group], water_topright2)

    player = Player((206, 1732), [visible_group, player_group], obstacle_group)
    boss = Boss((3208, 182), [boss_group], obstacle_group)

    def enemies():
        e1 = Enemy((3*64, 3*64), [visible_group, enemy_group], obstacle_group)
        e2 = Enemy((5*64, 3*64), [visible_group, enemy_group], obstacle_group)
        e3 = Enemy((14*64, 3*64), [visible_group, enemy_group], obstacle_group)
        e4 = Enemy((16*64, 3*64), [visible_group, enemy_group], obstacle_group)
        e5 = Enemy((26*64, 24*64), [visible_group, enemy_group], obstacle_group)
        e6 = Enemy((28*64, 24*64), [visible_group, enemy_group], obstacle_group)
        e7 = Enemy((56*64, 29*64), [visible_group, enemy_group], obstacle_group)
        e8 = Enemy((58*64, 29*64), [visible_group, enemy_group], obstacle_group)

    pos = 3136
        # HUD
    msc_border = pygame.image.load('mainPictures/msc_border.png').convert_alpha()
    msc_border = pygame.transform.scale(msc_border, (203, 133))
    attack_up = pygame.transform.scale(attack_up, (42, 46))
    ammo = pygame.transform.scale(ammo, (42, 42))
    health_border = pygame.Rect(10, 10, (player.max_health * 5) + 10, 25)

        # Spawn variables
    boss_spawn = False
    boss_music = False
    cloak_spawn = False
    key_spawn = False
    enemy_spawn = False
    enemy_spawn_flag = False
    shoot_time = 10

    while running:

        screen.fill(bg_colour)
        print(player.kills)
            # Boss spawn
        if player.rect.x > 2368 and player.rect.y < 900 and not boss_spawn:    
            visible_group.add(boss)
            boss_spawn = True
            Block((pos, 1088), [visible_group, tile_group, obstacle_group], dead_tree)
            Block((pos +64, 1088), [visible_group, tile_group, obstacle_group], dead_tree)
            Block((pos +128, 1088), [visible_group,tile_group, obstacle_group], dead_tree)
            Block((pos +192, 1088), [visible_group,tile_group, obstacle_group], dead_tree)
            # Boss music
        if boss_spawn == True and not boss_music:
            if boss.alive:
                pygame.mixer.music.load('music/bossMusic.mp3')
                pygame.mixer.music.play(-1)
                boss_music = True    

        if boss.health <= 400 and not cloak_spawn:
            Tile((boss.rect.x - 15, boss.rect.centery - 40), visible_group, cloak)
            cloak_spawn = True
            # Boss attack
        if boss.alive:
            if boss.health <= 400:
                shoot_time -= 1
                if shoot_time <= 0:
                    boss.shoot()
                    shoot_time = 50
            # Key spawn
        if boss.alive == False and not key_spawn: 
            Key((boss.rect.centerx, boss.rect.centery), visible_group, key)
            key_spawn = True
            pygame.mixer.music.stop()

        if not enemy_spawn:
            enemies()
            enemy_spawn = True
            enemy_spawned_for_kills = True

        if enemy_spawn:
            if len(enemy_group) == 0 or (player.kills % 6 == 0 and player.kills != 0 and not enemy_spawned_for_kills):
                enemy_spawn = False
                enemy_spawned_for_kills = False


        bullet_group.custDraw(player)
        bullet_group.update()
        visible_group.custDraw(player)
        visible_group.update()
        
            # HUD
        player_health = pygame.Rect(13 ,13 , (player.health * 5) + 4, 19)
        screen.blit(msc_border, (5, 38))
        screen.blit(attack_up, (35, 110))
        screen.blit(ammo, (35, 55))
        pygame.draw.rect(screen, ('black'), health_border)
        pygame.draw.rect(screen, ('red'), player_health)
        text('x ' + str(player.ammo), font, ('black'), screen, 100, 54)
        text('x ' + str(round(player.attack_up)), font, ('dark red'), screen, 100, 115)
        attack = str(round(player.attack_up))

        if player.alive:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SONG_END: # the current song has finished playing
                    current_song_index = (current_song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if boss.alive and boss_music:
                            pygame.mixer.music.fadeout(1000)
                            running = False
                        else:
                            running = False
                    if event.key == pygame.K_p:
                        pause()
                    if event.key == pygame.K_r:
                        math_page()
                    if event.key == pygame.K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                
                    if event.key == pygame.K_SPACE:
                        if player.ammo > 0:
                            shoot_sfx.play()
                            bullet_group.add(player.create_bullet())
                            player.ammo -= 1
                        
                    player.health -= reduce_health * 5
                    reduce_health = 0

                    if player.health > player.max_health:
                        player.health = player.max_health
                    
                    if player.ammo < player.max_ammo:
                        player.ammo += add_bullets
                        add_bullets = 0
                        if player.ammo > player.max_ammo:
                            player.ammo = player.max_ammo
        else:
            game_over()
            running = False
        
        if player.rect.y < -64:
            running = False
        
        pygame.display.flip()
        clock.tick(FPS)

def game_over():
    global screen
    global songs
    global current_song_index
    global SONG_END
    global boss_spawn
    global boss
    running = True

        # images
    bg = (127, 0, 0)
    dark_border = pygame.image.load('mainPictures/go_border.png')
    dark_border = pygame.transform.scale(dark_border, (screen.get_width(), 250))
    go_rect = dark_border.get_rect(center = (screen.get_width()//2, screen.get_height()//2))
    you_died = pygame.image.load('mainPictures/youDied.png')
    yd_rect = you_died.get_rect(center = (screen.get_width()//2, screen.get_height()//2))
    time = 90
    
    while running:
        time -= 1
        dark_border.set_alpha(7)
        you_died.set_alpha(20)
        screen.blit(dark_border, go_rect)
        if time <= 0:
            screen.blit(you_died, yd_rect)
            time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END: # the current song has finished playing
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if time <= 0:
                if event.type == pygame.KEYDOWN:
                    if boss.alive and boss_spawn:
                        pygame.mixer.music.fadeout(1000)
                        running = False
                    else:
                        running = False

        pygame.display.flip()
        clock.tick(FPS)

def math_page():
    global screen
    global songs
    global current_song_index
    global SONG_END
    global add_bullets
    global reduce_health

    running = True
        # images
    attack_up = pygame.image.load('mainPictures/attackUp.png').convert_alpha()
    ammo = pygame.image.load("mainSprites/bullet.png").convert_alpha()
    base_font = pygame.font.SysFont('arial', 50, True)
    correct_tick = pygame.image.load('mainPictures/correct.png').convert_alpha()
    wrong_x = pygame.image.load('mainPictures/wrong.png').convert_alpha()
    dark_border = pygame.image.load('mainPictures/go_border.png').convert_alpha()
    dark_border = pygame.transform.scale(dark_border, (screen.get_width(), screen.get_height()))
    db_rect = dark_border.get_rect()
    book = pygame.image.load('mainPictures/book.png').convert_alpha()
    book_rect = book.get_rect(center = (screen.get_width()//2, screen.get_height()//2))
    time1 = 50
    time2 = 60
    user_text = ''
    input_rect = pygame.Rect(800, (screen.get_height()//2) - 25, 1, 1)

    def generate_question():
        # Generate random arithmetic question
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*', '/'])
        
        if operator == '/':
            # Ensure division results in an integer
            while num2 == 0 or num1 % num2 != 0:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
            result = num1 // num2
            question = f"{num1} {operator} {num2} = "
        else:
            result = eval(f"{num1} {operator} {num2}")
            question = f"{num1} {operator} {num2} = "
        
        return question, str(result)
    
    questions, answer = generate_question()

        # HUD
    msc_border = pygame.image.load('mainPictures/msc_border.png').convert_alpha()
    msc_border = pygame.transform.scale(msc_border, (203, 133))
    attack_up = pygame.transform.scale(attack_up, (42, 46))
    ammo = pygame.transform.scale(ammo, (42, 42))
    health_border = pygame.Rect(10, 10, (player.max_health * 5) + 10, 25)
    
    while running:
        dark_border.set_alpha(10)
        book.set_alpha(40)
        screen.blit(dark_border, db_rect)
        time1 -= 1
        if time1 <= 0:
            screen.blit(book, book_rect)
            time1 = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END: # the current song has finished playing
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                if event.unicode.isdigit() or event.unicode == '.' or event.unicode == '-':
                    user_text += event.unicode
                if event.unicode == '\r':
                    if user_text == answer:
                        if player.health != player.max_health:
                            player.health += 5
                        else:
                            player.health = player.max_health
                        add_bullets += 3
                        screen.blit(correct_tick, (1030,(screen.get_height()//2) - 25))
                        questions, answer = generate_question()
                    else:
                        if player.health <= 0:
                            running = False
                        else:
                            player.health -= 5
                        screen.blit(wrong_x, (1030, (screen.get_height()//2) - 25))
                        questions, answer = generate_question()
                    user_text = ''
            # render random questions            
        question = base_font.render(questions, True, ('black'))
        time2 -= 1
        if time2 <= 0:
            question_rect = question.get_rect(topleft = (305, (screen.get_height()//2) - 25))
            screen.blit(question, question_rect)
            text_surface = base_font.render(user_text, True, ('black'))
            pygame.draw.rect(screen, (230, 209, 166), input_rect)
            screen.blit(text_surface, (input_rect.x +5, input_rect.y -5))
            time2 =0
        
            # HUD
        bullets = player.ammo + add_bullets
        if bullets > player.max_ammo:
            bullets = player.max_ammo
        
        player_health = pygame.Rect(13 ,13 , (player.health * 5) + 4, 19)
        screen.blit(msc_border, (5, 38))
        screen.blit(attack_up, (35, 110))
        screen.blit(ammo, (35, 55))
        pygame.draw.rect(screen, ('black'), health_border)
        pygame.draw.rect(screen, ('red'), player_health)
        text('x ' + str(bullets), font, ('black'), screen, 100, 54)
        text('x ' + attack, font, ('dark red'), screen, 100, 115)

        pygame.display.flip()
        clock.tick(FPS)

mainMenu()