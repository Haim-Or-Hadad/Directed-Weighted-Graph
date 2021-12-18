from Node import Node
from GraphInterface import GraphInterface


def v_size():
    """
    return the number of nodes in graph
    :return: the number of nodes in graph
    """
    return len(self.nodes)


class DiGraph:
    def __init__(self, **kwargs):
        self.nodes = dict()
        self.num_of_edge = 0
        self.mc = 0

    def e_size(self):
        """
        return the number of edges in graph
        :return: num_of_edge
        """
        return self.num_of_edge

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph,
            each node is represented using a pair
            (node_id, node_data)
            """
        self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """

        :param id1:
        :return:
        """
        if self.nodes.get(id1) is None:
            raise Exception('node:{}'.format(id1))
        return self.nodes.get(self, id1).connect_in()

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if self.nodes.get(id1) is None:
            raise Exception('node:{}'.format(id1))
        return self.nodes.get(id1).connect_out

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise NotImplementedError
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        if self.nodes.get(id1) is None:
            return False
        if self.nodes.get(id2) is None:
            return False
        self.num_of_edge + 1
        self.mc + 1
        self.nodes.get(id1).add_connect_out(id2, weight)
        self.nodes.get(id2).add_connect_in(id1, weight)
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id in self.nodes:
            return False
        self.mc += 1
        node = Node(node_id, pos)
        self.nodes[node_id] = node
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        removed_node = self.nodes[node_id]
        for dist in removed_node.connect_out.keys():
            self.remove_edge(node_id, dist)
        for source in removed_node.connect_in.keys():
            self.remove_edge(source, node_id)
        del self.nodes[node_id]
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        return True;

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        return True

# g = DiGraph()# for f in g.edges:
#     print(f.src)
# print(g.nodes[1].id)
# for e in edges:
#     print(e)
#
# for n in nodes:
#     print(n)
