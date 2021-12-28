import itertools
import json
import math
import random
import sys
from ctypes.wintypes import RGB
from queue import PriorityQueue
from tkinter import filedialog, Tk
from typing import List
from easygui import *
import pygame
from pygame import MOUSEBUTTONDOWN

from src.Button import Button
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph

bg = pygame.image.load("../src/nodebook.jpg")
Icon = pygame.image.load("../src/graph_icon.jpg")

WIDTH, HEIGHT = 900, 720


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph


    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        my_graph = DiGraph()
        try:
            with open(file_name, 'r') as file:
                g_dict = json.load(file)
                for node in g_dict['Nodes']:
                    if "pos" in node:
                        my_graph.add_node(node['id'], node['pos'])
                    else:
                        x = random.uniform(32, 33)
                        y = random.uniform(34, 36)
                        my_graph.add_node(node['id'], (x, y, 0))

                for edge in g_dict['Edges']:
                    my_graph.add_edge(edge["src"], edge["dest"], edge["w"])
                self.graph = my_graph
                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            Nodes = []  # List of Nodes and Edges.
            Edges = []
            # Going over all the nodes in the graph
            for node in self.graph.get_all_v().values():
                Nodes.append({"pos": node.pos, "id": node.id})  # add the node to the list
                # going over all the edges going out of the current node
                # edge_Dest is the key of the dest of the edge
                for edges_Dest in self.graph.all_out_edges_of_node(node.id):
                    # get the weight of the edge
                    weight = self.graph.all_out_edges_of_node(node.id)[edges_Dest]
                    Edges.append({"src": node.id, "w": weight, "dest": edges_Dest})
            # create a dictionary contain Node list and Edge list
            json_dict = {"Nodes": Nodes, "Edges": Edges}
            with open("../data/" + file_name + ".json", 'w') as file:
                # create the json file
                json.dump(json_dict, indent=4, fp=file)
        except IOError as e:
            print(e)
            return False
        return True

    def __str__(self):
        string = ''
        for node in self.graph.nodes.items():
            string += str(node)
        return string

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        This function using Dijkstra algorithm for finding the dist of id1 from all the nodes in the graph
        then going over the tags in id2 node back to id1 node adding the node id to the path
        """
        if id1 not in self.graph.nodes or id2 not in self.graph.nodes:
            return float('inf'), []
        self.dijkstra(id1)
        curr_node = self.graph.nodes[id2]
        weight = self.graph.nodes[id2].weight
        if weight == float('inf'):
            return float('inf'), []
        path = []
        while curr_node.id != id1:
            path.append(curr_node.id)
            tag = curr_node.tag
            curr_node = self.graph.nodes.get(tag)
        path.append(curr_node.id)
        path.reverse()
        return weight, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        perm = list(itertools.permutations(node_lst))  # create a list with all the permutations
        min_dist = math.inf  # set the min distance to max
        for perm in perm:  # go over all the permutations
            distance_sum = 0
            for nodes in range(len(perm) - 1):  # go over the nodes in the current permutation
                src = int(perm[nodes])
                dest = int(perm[nodes + 1])
                # sum the distance of the shortest path going over all the nodes in the curr permutations
                distance_sum += self.shortest_path(src, dest)[0]
            if distance_sum <= min_dist:
                min_dist = distance_sum
                ans = (perm, min_dist)
                if min_dist == math.inf:
                    ans = ([], min_dist)

        return ans

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        for key in self.graph.nodes.values():
            self.dijkstra(key.id)
        min_value = sys.maxsize
        for w in self.graph.nodes.values():
            if w.max_weight < min_value:
                t = (w.id, w.max_weight)
                min_value = w.max_weight

        return t

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        The random selection is written in the load from json function
        @return: None
        """
        # gui = GUI(self)
        # gui.gui()
        self.gui()

    def rest_tag_weight(self):
        """
        Rest tag and weight for dijkstra usage
        """
        for node in self.graph.nodes.values():
            node.weight = float('inf')
            node.tag = -1
            node.info = "White"

    def dijkstra(self, src: int):
        """
        Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes
        in a graph,
         :param src:source node
          :return:update at each node the minimum weight of the shortest path from src
        """
        self.rest_tag_weight()
        self.graph.nodes.get(src).weight = 0
        node_queue = PriorityQueue()
        node_queue.put((self.graph.nodes.get(src).weight, self.graph.nodes.get(src)))
        while not node_queue.empty():
            node = node_queue.get()[1]
            node.info = "Black"
            for neigh in node.connect_out:
                if self.graph.nodes.get(neigh).info == "White":
                    if node.weight + node.connect_out[neigh] < self.graph.nodes[neigh].weight:
                        self.graph.nodes.get(neigh).weight = node.weight + node.connect_out[neigh]
                        self.graph.nodes.get(neigh).tag = node.id
                        node_queue.put((self.graph.nodes.get(neigh).weight, self.graph.nodes.get(neigh)))

        for node in self.graph.nodes.values():
            if node.weight > self.graph.nodes.get(src).max_weight:
                self.graph.nodes.get(src).max_weight = node.weight

    def gui(self):
        pygame.init()
        scr = pygame.display.set_mode((900, 600))
        pygame.font.init()
        pygame.display.set_icon(Icon)
        pygame.display.set_caption('Graph GUI')
        run = True
        while run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                scr.blit(bg, (0, 0))
                self.algorithms_buttons(e, scr)
                if e.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.operation(pos, scr)
            self.draw_nodes(scr)
            self.draw_edges(scr)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def algorithms_buttons(self, e, scr):
        save = Button('save', (100, 50))
        load = Button('load', (100, 50))
        TSP = Button('TSP', (100, 50))
        shortest_path = Button('s-path', (100, 50))
        center = Button('center', (100, 50))
        #######save########
        save.render(scr, (800, 0))
        #######load########
        load.render(scr, (800, 50))
        #####TSP#########
        TSP.render(scr, (800, 100))
        #####shortest_path####
        shortest_path.render(scr, (800, 150))
        ######center####
        center.render(scr, (800, 200))
        add = Button("add node", (160, 60))
        remove = Button("remove node", (160, 60))
        add_edge = Button("add edge", (160, 60))
        remove_edge = Button("remove edge", (160, 60))
        #####add######
        add.render(scr, (740, 540))
        #####remove######
        remove.render(scr, (580, 540))
        ####add edge###
        add_edge.render(scr, (740, 480))
        ####remove edge###
        remove_edge.render(scr, (740, 420))

    def operation(self, pos, scr):
        if 800 < pos[0] < 900 and 0 < pos[1] < 50:  # for save function
            title = "save file"
            output = enterbox("enter new name of file", title)
            message = str(output)
            self.save_to_json(message)
        if 800 < pos[0] < 900 and 50 < pos[1] < 100:  # for load func
            root = Tk()
            file_path = filedialog.askopenfilename()
            root.destroy()
            self.load_from_json(file_path)
        if 800 < pos[0] < 900 and 100 < pos[1] < 150:  # for TSP
            list_for_tsp = list((enterbox("enter list with comma between every node")).split(","))
            tsp = self.TSP(list_for_tsp)
            title = "Message Box"
            message = "Entered Name : " + str(tsp)
            msg = msgbox(message, title)

        if 800 < pos[0] < 900 and 150 < pos[1] < 200:  # for s-path
            _id1, _id2 = enterbox("enter id1"), enterbox("enter id2")
            answer = self.shortest_path(int(_id1), int(_id2))
            title = "Message Box"
            message = "Entered Name : " + str(answer)
            msg = msgbox(message, title)
        if 800 < pos[0] < 900 and 200 < pos[1] < 250:  # for center
            t = self.centerPoint()
            _x = self.graph.nodes.get(t[0]).x()
            _y = self.graph.nodes.get(t[0]).y()
            _x = self.my_scale(_x, x=True)
            _y = self.my_scale(_y, y=True)
            tup = (_x, _y)
            # message = "Center: " + str(t)
            # msg = msgbox(message, "Center")
            pygame.draw.circle(scr, RGB(200, 80, 0), tup, 10)

        if 740 < pos[0] < 900 and 540 < pos[1] < 600:  # for add node
            _id, _x, _y = int(enterbox("enter new node_id ")), enterbox("enter x"), enterbox("enter y")
            _pos = (_x + "," + _y + "," + '0')
            self.graph.add_node(_id, _pos)
        if 590 < pos[0] < 740 and 540 < pos[1] < 600:  # for remove node
            title = "Remove Node"
            output = enterbox("enter node_id that yow want to remove", title)
            message = str(output)
            self.graph.remove_node(int(message))
        if 740 < pos[0] < 900 and 480 < pos[1] < 540:
            title = "Add Edge"
            _id1, _id2, w = int(enterbox("enter id1", title)) \
                , int(enterbox("enter id2 ", title)), float(enterbox("weight"))
            self.graph.add_edge(_id1, _id2, w)
        if 740 < pos[0] < 900 and 420 < pos[1] < 480:
            title = "Remove Edge"
            _id1, _id2 = int(enterbox("enter id1", title)), int(enterbox("enter id2 ", title))
            self.graph.remove_edge(_id1, _id2)

    def draw_nodes(self, scr):
        for node in self.graph.nodes.values():
            x = self.my_scale(node.x(), x=True)
            y = self.my_scale(node.y(), y=True)
            t = (x, y)
            pygame.draw.circle(scr, RGB(40, 40, 40), t, 6)

    def draw_edges(self, scr):
        for e in self.graph.nodes.values():
            src_x = e.x()
            src_y = e.y()
            list_out = self.graph.all_out_edges_of_node(e.id)
            src_x = self.my_scale(src_x, x=True)
            src_y = self.my_scale(src_y, y=True)
            for edge in list_out:
                dest_x = self.graph.nodes.get(edge).x()
                dest_y = self.graph.nodes.get(edge).y()
                dest_x = self.my_scale(dest_x, x=True)
                dest_y = self.my_scale(dest_y, y=True)
                # t1,t2 = (src_x, src_y), (dest_x, dest_y)
                pygame.draw.line(scr, RGB(0, 0, 0), (src_x, src_y), (dest_x, dest_y), 1)
                rotation = math.degrees(math.atan2(src_y - dest_y, dest_x - src_x)) + 90
                pygame.draw.polygon(scr, (120, 120, 130), (
                    (dest_x + 0.5 * math.sin(math.radians(rotation)), dest_y + 0.5 * math.cos(math.radians(rotation))),
                    (
                        dest_x + 15 * math.sin(math.radians(rotation - 158)),
                        dest_y + 15 * math.cos(math.radians(rotation - 158))),
                    (dest_x + 15 * math.sin(math.radians(rotation + 158)),
                     dest_y + 15 * math.cos(math.radians(rotation + 158)))))

                # pygame.draw.line(scr, RGB(40, 40, 40),
                #                  (src_x, src_y), (dest_x, dest_y))

    def draw_arrow(self, screen, colour, start, end):
        pygame.draw.line(screen, colour, start, end, 2)
        rotation = math.degrees(math.atan2(start[1] - end[1], end[0] - start[0])) + 90
        pygame.draw.polygon(screen, (255, 0, 0), (
            (end[0] + 20 * math.sin(math.radians(rotation)), end[1] + 20 * math.cos(math.radians(rotation))),
            (
                end[0] + 20 * math.sin(math.radians(rotation - 120)),
                end[1] + 20 * math.cos(math.radians(rotation - 120))),
            (end[0] + 20 * math.sin(math.radians(rotation + 120)),
             end[1] + 20 * math.cos(math.radians(rotation + 120)))))
    #####Scale functions#######
    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, 680, self.min_x(), self.max_x())
        if y:
            return self.scale(data, 50, 600 - 50, self.min_y(), self.max_y())

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def min_x(self):
        min_x = sys.maxsize
        for node in self.graph.nodes.values():
            if float(node.x()) < min_x:
                min_x = float(node.x())
        return min_x

    def max_x(self):
        max_x = 0
        for node in self.graph.nodes.values():
            if node.x() > max_x:
                max_x = node.x()
        return max_x

    def min_y(self):
        min_y = sys.maxsize
        for node in self.graph.nodes.values():
            if node.y() < min_y:
                min_y = node.y()
        return min_y

    def max_y(self):
        max_y = 0
        for node in self.graph.nodes.values():
            if node.y() > max_y:
                max_y = node.y()
        return max_y
