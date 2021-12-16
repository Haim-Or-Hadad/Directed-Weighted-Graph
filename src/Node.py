import json
import os


class Node:
    def __init__(self, pos , id):
        """
        pos: the position of nodes in space.
        id: node's key
        """
        self.pos = pos
        self.id = id
        self.connect_out = {}
        self.connect_in = {}

    def get_id(self):
        """
        :returns node's id.
        return:id
        """
        return self.id

    def get_pos(self):
        """
        return node's position
        :return:pos
        """
        return self.pos

    def add_connet_out(self , id , weight):
        """
        add edge between this node to neighbor node
        :param id: neighbor id
        :param weight: weight id
        """
        self.connect_to[id] = weight

    def add_connect_in(self , id , weight):
        """
        add edge that connect to this node
        :param id: neighbor id
        :param weight: weight id
        """
        self.connect_in[id] = weight






# root_path = os.path.dirname(os.path.abspath(__file__))
#
#
# with open(root_path+'\A0.JSON', 'r') as file:
#     list_nodes = json.load(file)['Nodes']
#     nodes = [Node(**n) for n in list_nodes]

# for n in nodes:
#     print(n.pos , n.id)
