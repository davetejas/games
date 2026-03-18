import pygame
from settings import *

class Board:
    def __init__(self, rows, cols, tile_size, pos):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.pos = pos  # top-left position on screen
        self.total_tiles = rows * cols

        # Define tile types in a simple repeating pattern
        self.tile_types = []
        for i in range(self.total_tiles):
            if i == self.total_tiles - 1:
                self.tile_types.append("end")
            elif i % 5 == 0:
                self.tile_types.append("vp")      # victory point tile
            elif i % 7 == 0:
                self.tile_types.append("card")    # card tile
            else:
                self.tile_types.append("normal")

    def index_to_row_col(self, index):
        row = index // self.cols
        col = index % self.cols
        return row, col

    def get_tile_rect(self, index):
        row, col = self.index_to_row_col(index)
        x = self.pos[0] + col * self.tile_size
        y = self.pos[1] + row * self.tile_size
        return pygame.Rect(x, y, self.tile_size, self.tile_size)

    def draw(self, screen):
        for i in range(self.total_tiles):
            rect = self.get_tile_rect(i)
            tile_type = self.tile_types[i]

            if tile_type == "start":
                color = (200, 255, 200)
            elif tile_type == "end":
                color = (255, 215, 0)  # golden for the end
            elif tile_type == "vp":
                color = (255, 240, 200)  # light yellow
            elif tile_type == "card":
                color = (220, 220, 255)  # light blue
            else:
                color = (230, 230, 230)  # neutral

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
