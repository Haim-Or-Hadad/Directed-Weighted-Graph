import json
import os
import pygame
from pygame import Color, display, gfxdraw
from pygame.constants import RESIZABLE
#from Node import nodes
from Node import Node




class DiGraph:
    def __init__(self):
        self.nodes = dict()
        self.num_of_edge = 0

    def size_e(self):
        """
        return the number of edges in graph
        :return: num_of_edge
        """
        return self.num_of_edge

    def size_v(self):
        """
        return the number of nodes in graph
        :return: the number of nodes in graph
        """
        return self.nodes.__len__()



# g = DiGraph()# for f in g.edges:
#     print(f.src)
#print(g.nodes[1].id)
# for e in edges:
#     print(e)
#
# for n in nodes:
#     print(n)