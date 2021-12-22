import sys
from ctypes.wintypes import RGB

import pygame

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

bg = pygame.image.load("nodebook.jpg")


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


def gui(gra_algo: GraphAlgo = GraphAlgo()):
    # min_x = min(list(gra_algo.graph.nodes), key=lambda n: n.pos.x).pos.x
    # min_y = min(list(gra_algo.graph.nodes), key=lambda n: n.pos.y).pos.y
    # max_x = max(list(gra_algo.graph.nodes), key=lambda n: n.pos.x).pos.x
    # max_y = max(list(gra_algo.graph.nodes), key=lambda n: n.pos.y).pos.y
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
        for node in gra_algo.graph.nodes.values():
            position = eval(node.pos)
            # x = scale(position[0],0 , 600 , min_x , max_x)
            # y = scale(position[1],0 , 500, min_y,max_y)
            pygame.draw.circle(scr, RGB(40, 40, 40), position[:2], 80)

        pygame.display.update()

    pygame.quit()
    sys.exit()


g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
file = "../data/A5.json"
g_algo.load_from_json(file)
gui(g_algo)
