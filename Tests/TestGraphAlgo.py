import unittest
from math import inf

from src.DiGraph import DiGraph
from data import *

from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    graph = DiGraph()
    test_graph = GraphAlgo(graph)

    def test1_load_from_json(self):
        self.assertTrue(self.test_graph.load_from_json("../data/A1.json"))
        self.assertTrue(self.test_graph.load_from_json('../data/A2.json'))
        self.assertTrue(self.test_graph.load_from_json('../data/A3.json'))
        self.assertTrue(self.test_graph.load_from_json('../data/A4.json'))
        self.assertTrue(self.test_graph.load_from_json('../data/A5.json'))

    def test2_save_to_json(self):
        self.assertTrue(self.test_graph.load_from_json('../data/A1.json'))
        self.assertTrue(self.test_graph.save_to_json('../data/A1_saved'))
        self.assertTrue(self.test_graph.load_from_json('../data/A2.json'))
        self.assertTrue(self.test_graph.save_to_json('../data/A2_saved'))
        self.assertTrue(self.test_graph.load_from_json('../data/A3.json'))
        self.assertTrue(self.test_graph.save_to_json('../data/A3_saved'))
        self.assertTrue(self.test_graph.load_from_json('../data/A4.json'))
        self.assertTrue(self.test_graph.save_to_json('../data/A4_saved'))
        self.assertTrue(self.test_graph.load_from_json('../data/A5.json'))
        self.assertTrue(self.test_graph.save_to_json('../data/A5_saved'))

    def test3_shortest_path(self):
        self.test_graph.load_from_json('../data/G1.json')
        self.assertEqual((8.718425478533105, [2, 6, 7, 8, 9, 10, 11]), self.test_graph.shortest_path(2, 11))
        self.test_graph.graph.remove_node(0)
        self.test_graph.graph.remove_node(15)
        self.assertEqual((inf, []), self.test_graph.shortest_path(16, 4))

    def test3_TSP(self):
        self.test_graph.load_from_json('../data/G1.json')
        self.assertEqual(((3, 6, 10, 15), 15.769026561393964), self.test_graph.TSP([3, 6, 10, 15]))
        self.test_graph.graph.remove_node(0)
        self.test_graph.graph.remove_node(15)
        self.assertEqual(([], inf), self.test_graph.TSP([16, 2, 7]))

    def test4_centerPoint(self):
        self.test_graph.load_from_json('../data/G1.json')
        self.assertEqual((8, 9.925289024973141), self.test_graph.centerPoint())

    if __name__ == '__main__':
        unittest.main()
