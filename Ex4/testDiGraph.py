import json
import threading
import unittest
from Ex4.GraphAlgo import GraphAlgo
from Ex4.GraphView import GraphView

class MyTestCase(unittest.TestCase):

    def test_v_size(self):
        a = GraphAlgo()
        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().v_size(), 40)
        f.close()

        f = open('../data/A2')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().v_size(), 31)
        f.close()

        f = open('../data/A1')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().v_size(), 17)
        f.close()

        f = open('../data/A0')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().v_size(), 11)
        f.close()

    def test_e_size(self):
        a = GraphAlgo()
        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().e_size(), 102)
        f.close()

        f = open('../data/A2')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().e_size(), 80)
        f.close()

        f = open('../data/A1')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().e_size(), 36)
        f.close()

        f = open('../data/A0')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().e_size(), 22)
        f.close()

    def test_pokemons_size(self):
        f = open('../data/A0')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        # take from pokemon json example in "client"
        a_list = {"Pokemons": [
            {"Pokemon": {"value": 5.0, "type": -1, "pos": "35.197656770719604,32.10191878639921,0.0"}}]}
        a.load_from_json_pokemons(a_list)
        f.close()
        self.assertEqual(a.get_graph().pokemons_size(), 1)  # add assertion here

    def test_get_node_pos(self):
        f = open('../data/A0')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))

        self.assertEqual(a.get_graph().get_node_pos(10), ('35.18910131880549,32.103618700840336,0.0'))

    # #work good in testGraphAlgo - use there
    # def test_getNodeX(self):
    #     pass

    # # work good in testGraphAlgo - use there
    # def test_getNodeY(self):
    #     pass

    def test_get_all_v(self):
        f = open('../data/A0')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().get_all_v().get(3), '35.197528356739305,32.1053088,0.0')

    def test_all_in_edges_of_node(self):
        f = open('../data/A2')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().all_in_edges_of_node(6), {2: 1.7938753352369698, 5: 1.734311926030133, 7: 1.5786081900467002})
        self.assertEqual(a.get_graph().all_in_edges_of_node(6), {})
        f.close()

    def test_all_out_edges_of_node(self):
        f = open('../data/A2')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().all_in_edges_of_node(6), {2: 1.7938753352369698, 5: 1.734311926030133, 7: 1.5786081900467002})
        self.assertNotEqual(a.get_graph().all_in_edges_of_node(5),
                         {2: 1.7938753352369698, 5: 1.734311926030133, 7: 1.5786081900467002})
        f.close()


    def test_add_edge(self):
        f = open('../data/A2')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().add_edge(2, 4, 1.6855), True)
        self.assertEqual(a.get_graph().add_edge(2, 4, 1.685), False)
        f.close()


if __name__ == '__main__':
    unittest.main()


