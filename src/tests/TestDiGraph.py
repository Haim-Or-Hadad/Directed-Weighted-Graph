import unittest
from src.DiGraph import DiGraph
from src.Node import Node

class test(unittest.TestCase):
    test_graph = DiGraph()

    def test_add_node(self):
        self.test_graph.add_node(0, (1, 4, 0))
        self.test_graph.add_node(1,(1,4,6))
        self.test_graph.add_node(2,(1,4,6))
        self.test_graph.add_node(0, (1, 4, 6))
        pos1 = self.test_graph.nodes.values().get_pos()
        pos2 = self.test_graph.nodes.get(3).get_pos()
        self.assertEqual(pos1 , pos2 )

    if __name__ == '__main__':
        unittest.main()