import json

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    def _init_(self, graph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        my_graph = DiGraph()
        with open("path_to_file", 'r') as file:
            g_dict = json.load(file)
        "load the nodes from dict to our graph"
        for node in g_dict['nodes']:
            my_graph.add_node(node.id, node.pos)
