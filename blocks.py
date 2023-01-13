import os
import random

import pygame
from config import *

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
FPS = 60


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

    def get_click(self, pos):
        cell = self.get_cell(pos)
        self.on_click(cell)

    def get_cell(self, pos):
        x, y = pos
        if x < self.left or x > self.left + self.cell_size * self.width \
                or y < self.top or y > self.top + self.cell_size * self.height:
            return None
        else:
            cell_x = (x - self.left) // self.cell_size
            cell_y = (y - self.top) // self.cell_size
            return cell_x, cell_y

    def on_click(self, cell):
        if cell == None:
            print("None")
        else:
            cell_x, cell_y = cell
            print(cell_x, cell_y)
            self.board[cell_y][cell_x] = 0 if self.board[cell_y][cell_x] else 1


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


clock = pygame.time.Clock()


class Block(pygame.sprite.Sprite):
    last_update = pygame.time.get_ticks()
    image1 = load_block("pixil-frame-0_3.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


all_blocks = pygame.sprite.Group()
for i in range(20):
    all_blocks.add(Block(i * 40, 0))

for i in range(20):
    all_blocks.add(Block(i * 40, 80))

board = Board(20, 20)
running = True
while running:
    time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

    screen.fill(pygame.Color('black'))
    time += 1
    board.render(screen)
    all_blocks.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
