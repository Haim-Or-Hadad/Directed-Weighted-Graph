import unittest
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
    
    if __name__ == '__main__':
        unittest.main()
