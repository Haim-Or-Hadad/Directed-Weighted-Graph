import sys
from ctypes.wintypes import RGB

import pygame

from Node import Node
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

bg = pygame.image.load("nodebook.jpg")


class GUI:
    gra_algo: GraphAlgo = GraphAlgo()

    def scale(data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimensions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def gui(self, g):
        self.gra_algo = g
        min_x = self.min_x()
        min_y = self.min_y()
        max_x = self.max_x()
        max_y = self.max_x()
        pygame.init()
        scr = pygame.display.set_mode((600, 500))
        pygame.font.init()
        FONT = pygame.font.SysFont('Our Grapg', 20, bold=True)
        run = True
        while run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
            scr.blit(bg, (0, 0))
            # scr.fill(RGB(238,233,233))
            for node in self.gra_algo.graph.nodes.values():
                position = (node.x())
                x = self.scale(position[0], 0, 600, min_x, max_x)
                y = self.scale(position[1], 0, 500, min_y, max_y)
                pygame.draw.circle(scr, RGB(40, 40, 40), position[:1], 80)

            pygame.display.update()

        pygame.quit()
        sys.exit()

    def min_x(self):
        min_x = sys.maxsize
        for node in self.gra_algo.graph.nodes.values():
            if node.x() < min_x:
                min_x = node.x()
        return min_x

    def max_x(self):
        max_x = 0
        for node in self.gra_algo.graph.nodes.values():
            if node.x() > max_x:
                max_x = node.x()
        return max_x

    def min_y(self):
        min_y = sys.maxsize
        for node in self.gra_algo.graph.nodes.values():
            if node.y() < min_y:
                min_y = node.y()
        return min_y

    def max_y(self):
            max_y = 0
            for node in self.gra_algo.graph.nodes.values():
                if node.y() > max_y:
                    max_y = node.y()
            return max_y



    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/A5.json"
    g_algo.load_from_json(file)

