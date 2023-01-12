import os
import random

import pygame
from config import *

time = 0
pygame.display.set_caption("aaa-a-lab")
pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
FPS = 60
speed = 2
pygame.mixer.init()
pygame.mixer.music.load('The_past.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
move_right = move_left = move_up = move_down = False


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
    image = pygame.transform.smoothscale(image, (33, 33))
    return image


class Hero(pygame.sprite.Sprite):
    image1 = load_img(f"cha{0}.png")
    image2 = load_img(f"cha{1}.png")
    last_update = pygame.time.get_ticks()

    def __init__(self, x, y):
        super().__init__()
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if move_up and self.rect.y >= 4:
            self.rect.y -= speed
        if move_down and self.rect.y <= 760:
            self.rect.y += speed
        if move_left and self.rect.x >= -3:
            self.rect.x -= speed
        if move_right and self.rect.x <= 770:
            self.rect.x += speed
        self.rotate()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 550:
            self.last_update = now
            if self.image == self.image1:
                self.image = self.image2
            elif self.image == self.image2:
                self.image = self.image1


clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

all_sprites.add(Hero(50, 50))
board = Board(15, 15)
running = True
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

    screen.fill(pygame.Color('black'))
    board.render(screen)
    all_sprites.update()
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()