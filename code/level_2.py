import sys
from random import randrange
import sqlite3
import pygame
import subprocess
import time as t


if __name__ == '__main__':
    pygame.init()
    running = True
    time = 0
    pygame.display.set_caption("aaa-a-lab")
    pygame.init()
    size = width, height = 800, 900
    screen = pygame.display.set_mode(size)
    FPS = 60
    speed = 2.5
    pygame.mixer.init()
    pygame.mixer.music.load('../data/The_past.mp3')
    pygame.mixer.music.set_volume(0.02)
    pygame.mixer.music.play(loops=-1)
    move_right = move_left = move_up = move_down = False
    flag = False
    con = sqlite3.connect('../database/Coins.db')
    cur = con.cursor()
    cur.execute('UPDATE coins SET Coins = 0, Weapon = 0, Skin = 0, Hearts = 2')
    con.commit()


    def load_block(name, color_key=None):
        image = pygame.image.load(name)

        if color_key is not None:
            image.convert()
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (39, 39))
        return image


    class Board:
        # создание поля
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            # значения по умолчанию
            self.left = 0
            self.top = 0
            self.cell_size = 40

        # настройка внешнего вида
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size

        def render(self, screen):
            for cell_y in range(self.height):
                for cell_x in range(self.width):
                    x = self.left + self.cell_size * cell_x
                    y = self.top + self.cell_size * cell_y
                    if self.board[cell_y][cell_x]:
                        pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), width=0)
                    else:
                        pygame.draw.rect(screen, pygame.Color('white'), (x, y, self.cell_size, self.cell_size), width=1)

        def get_cell(self, pos):
            x, y = pos
            if x < self.left or x > self.left + self.cell_size * self.width \
                    or y < self.top or y > self.top + self.cell_size * self.height:
                return None
            else:
                cell_x = (x - self.left) // self.cell_size
                cell_y = (y - self.top) // self.cell_size
                return cell_x, cell_y


    def load_img(name, color_key=None):
        image = pygame.image.load(name)

        if color_key is not None:
            image.convert()
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (20, 20))
        return image


    def load_heart(name, color_key=None):
        image = pygame.image.load(name)

        if color_key is not None:
            image.convert()
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (60, 85))
        return image


    def load_spider(name, color_key=None):
        image = pygame.image.load(name)

        if color_key is not None:
            image.convert()
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (30, 30))
        return image


    class Block(pygame.sprite.Sprite):
        last_update = pygame.time.get_ticks()
        image1 = load_block("../data/pixil-frame-0_3.png")

        def __init__(self, x, y):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


    all_blocks = pygame.sprite.Group()


    def make_a_lyb():
        with open('level_2.txt', 'r') as f:
            lvl = f.read()
            lvl = lvl.split('\n')
            for i, j in enumerate(lvl):
                for x, y in enumerate(j):
                    if y == '#':
                        all_blocks.add(Block(i * 40, x * 40))

    make_a_lyb()
    coords = [(i.rect.x, i.rect.y) for i in all_blocks]


    class Hero(pygame.sprite.Sprite):
        heart = 2
        image1 = load_img(f"../data/cha{0}.png")
        image2 = load_img(f"../data/cha{1}.png")
        last_update = pygame.time.get_ticks()
        last_death = pygame.time.get_ticks()

        def __init__(self, x, y):
            super().__init__()
            self.con = sqlite3.connect('../database/Coins.db')
            self.cur = self.con.cursor()
            self.coins = 0
            self.start = [x, y]
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = speed
            self.coords = coords

        def update(self):
            if move_up and self.rect.y >= 4:
                self.rect.y -= self.speed
            if move_down and self.rect.y <= 760:
                self.rect.y += self.speed
            if move_left and self.rect.x >= -3:
                self.rect.x -= self.speed
            if move_right and self.rect.x <= 770:
                self.rect.x += self.speed
            self.rotate()
            if pygame.sprite.spritecollide(self, exit1, False):
                self.speed = 0
                self.cur.execute('UPDATE levels SET value = 1 WHERE id = 2')
                self.con.commit()
                termination()
            if len(all_hearts) == 1:
                if self.cur.execute('SELECT Hearts FROM coins').fetchone()[0] == 2:
                    all_hearts.add(heart2)
                    self.heart = 2
            if pygame.sprite.spritecollideany(self, all_blocks):
                self.rect.x = self.start[0]
                self.rect.y = self.start[1]
            if pygame.sprite.spritecollideany(self, exit1):
                global flag
                flag = True
            if self.cur.execute('SELECT Skin FROM coins').fetchone()[0] == 1:
                self.image = load_img('../data/new_skin.png')
            else:
                self.rotate()
            if self.cur.execute('SELECT Weapon FROM coins').fetchone()[0] == 1:
                if pygame.sprite.spritecollideany(self, all_spiders) is not None:
                    sprt = pygame.sprite.spritecollideany(self, all_spiders)
                    img = load_spider('../data/Кровь.png')
                    sprt.image = img
            else:
                if pygame.sprite.spritecollide(self, all_spiders, False) \
                        and pygame.time.get_ticks() - self.last_death > 2000:
                    self.last_death = pygame.time.get_ticks()
                    if self.heart == 2:
                        heart2.remove(all_hearts)
                        self.heart -= 1
                        self.cur.execute('UPDATE coins SET Hearts = 1')
                        self.con.commit()
                    else:
                        all_hearts.add(heart2)
                        self.cur.execute('UPDATE coins SET Coins = 0, Weapon = 0, Skin = 0, Hearts = 2')
                        self.con.commit()
                        self.rect.x = self.start[0]
                        self.rect.y = self.start[1]
                        self.heart = 2
                        for j in all_coins:
                            j.kill()
                        for j in range(7):
                            all_coins.add(Coins())
            if pygame.sprite.spritecollide(self, all_coins, True):
                self.coins += 1
                self.cur.execute('UPDATE coins SET Coins = ?', (self.coins,))
                self.con.commit()
            if pygame.sprite.spritecollide(self, trader, False):
                self.rect.x -= 40
                t.sleep(0.5)
                subprocess.Popen(['python', 'trader.py'])

        def rotate(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 550:
                self.last_update = now
                if self.image == self.image1:
                    self.image = self.image2
                elif self.image == self.image2:
                    self.image = self.image1

    def termination():
        global running
        running = False

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    hero = Hero(50, 770)
    all_sprites.add(hero)
    exit1 = pygame.sprite.Group()

    class Exit1(pygame.sprite.Sprite):
        image1 = load_img("../data/door.png")
        image1 = pygame.transform.smoothscale(image1, (20, 40))

        def __init__(self):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = 780
            self.rect.y = 40


    exit1.add(Exit1())


    class Hearts(pygame.sprite.Sprite):
        image1 = load_heart("../data/heart.png")

        def __init__(self, x, y):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


    heart1 = Hearts(650, 800)
    heart2 = Hearts(720, 800)
    all_hearts = pygame.sprite.Group()
    all_hearts.add(heart1)
    all_hearts.add(heart2)


    class Trader(pygame.sprite.Sprite):
        image1 = pygame.image.load('../data/trader.png')

        def __init__(self):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = 170
            self.rect.y = 365

    trader = pygame.sprite.Group()
    trader.add(Trader())


    class Spiders(pygame.sprite.Sprite):
        image1 = load_spider("../data/spide.png")

        def __init__(self):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.y = randrange(5, 800, 40)
            self.rect.x = randrange(5, 800, 40)
            while pygame.sprite.spritecollideany(self, all_blocks) \
                    or pygame.sprite.spritecollideany(self, all_sprites) \
                    or pygame.sprite.spritecollideany(self, trader):
                self.rect.y = randrange(5, 800, 40)
                self.rect.x = randrange(5, 800, 40)


    all_spiders = pygame.sprite.Group()

    for i in range(5):
        all_spiders.add(Spiders())


    class Coins(pygame.sprite.Sprite):
        image1 = load_img("../data/coin.png")
        last_update = pygame.time.get_ticks()

        def __init__(self):
            super().__init__()
            self.image = self.image1
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = 20
            while pygame.sprite.spritecollideany(self, all_blocks) \
                    or pygame.sprite.spritecollideany(self, all_sprites) \
                    or pygame.sprite.spritecollideany(self, all_spiders) \
                    or pygame.sprite.spritecollideany(self, trader) \
                    or pygame.sprite.spritecollideany(self, exit1):
                self.rect.y = randrange(10, 800, 40)
                self.rect.x = randrange(10, 800, 40)


    all_coins = pygame.sprite.Group()
    for i in range(7):
        all_coins.add(Coins())

    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)

    board = Board(20, 20)
    while running:
        time = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                if event.key == pygame.K_a:
                    move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False
                if event.key == pygame.K_a:
                    move_left = False
        screen.fill(pygame.Color('black'))
        board.render(screen)
        all_blocks.draw(screen)
        all_sprites.draw(screen)
        exit1.draw(screen)
        all_sprites.update()
        pygame.draw.rect(screen, [150, 75, 50], [0, 801, 800, 900])
        all_spiders.draw(screen)
        all_hearts.draw(screen)
        trader.draw(screen)
        all_coins.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()
    sys.excepthook = except_hook
    pygame.quit()
