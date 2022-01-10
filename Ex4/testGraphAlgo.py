import json
import unittest
from Ex4.GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):

    def test_get_graph(self):
        f = open('../data/A0')
        a = GraphAlgo()
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.get_graph().v_size(), 11)
        f.close()

    def test_load_from_json_graph(self):
        f = open('../data/A0')
        a = GraphAlgo()
        self.assertEqual(a.load_from_json_graph(json.load(f)), True)
        f.close()
        f = open('../data/A1')
        self.assertEqual(a.load_from_json_graph(json.load(f)), True)
        f.close()
        f = open('../data/A2')
        self.assertEqual(a.load_from_json_graph(json.load(f)), True)
        f.close()
        f = open('../data/A3')
        self.assertEqual(a.load_from_json_graph(json.load(f)), True)
        f.close()


    def test_distance(self):
        a = GraphAlgo()
        self.assertEqual(a.distance("35.18753053591606,32.10378225882353,0.0", "35.18958953510896,32.10785303529412,0.0"), 0.0045618744776541025)
        self.assertNotEqual(
            a.distance("35.18753053591606,32.10378225882353,0.0", "35.18958953510896,32.10785303529412,0.0"),
            0.00045618744776541025)

    def test_lengthPointX(self):
        a = GraphAlgo()
        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        x = a.get_graph().getNodeX(0)  # 35.18750930912026
        x1 = a.get_graph().getNodeX(1)  # 35.18961076190476
        self.assertEqual(a.length_point_x(x, x1), 0.0021014527844986984)
        f.close()

    def test_lengthPointY(self):
        a = GraphAlgo()
        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        y = a.get_graph().getNodeY(0)  # 32.10374591260504
        y1 = a.get_graph().getNodeY(1)  # 32.10794390084033
        self.assertEqual(a.length_point_y(y, y1), 0.004197988235286435)
        f.close()

    def test_lengthBetween2Segment(self):
        a = GraphAlgo()
        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        x = a.length_point_x(a.get_graph().getNodeX(0), a.get_graph().getNodeX(1))  # 0.0021014527844986984
        y = a.length_point_y(a.get_graph().getNodeY(0), a.get_graph().getNodeY(1))  # 0.004197988235286435
        self.assertEqual(a.length_between2_segment(x, y), 0.002096535450787736)
        f.close()

    def test_contains(self):
        a = GraphAlgo()
        pos1 = "35.21315127845036,32.10427293277311,0.0"  #id 11 in graph A3
        pos2 = "35.212620608555284,32.10719880336134,0.0" #id 39 in graph A3
        pos3 = "35.21219607263922,32.10616293613445,0.0"  # id 10 in graph A3 - contain in edge 11-39
        self.assertLess(a.contains(pos1, pos2, pos3),  0.01)
        pos1 = "35.18725458757062,32.109306884033614,0.0"  # id 26 in graph A3
        pos2 = "35.18806120581114,32.099711482352944,0.0"  # id 27 in graph A3
        pos3 = "35.18750930912026,32.10374591260504,0.0"  # id 0 in graph A3 - is closer but not contain in edge 11-39
        self.assertGreater(a.contains(pos1, pos2, pos3), 0.01)

    def test_load_from_json_pokemons(self):
        a = GraphAlgo()
        a_list = {}
        try:
            # take from pokemon json example in "client"
            a_list = {"Pokemons": [
                {"Pokemon": {"value": 5.0, "type": -1, "pos": "35.197656770719604,32.10191878639921,0.0"}}]}
            json_string = json.dumps(a_list)
            json_file = open("../data/pokemon.json", "w")
            json_file.write(json_string)
            json_file.close()
        except:
            print("Error")

        self.assertEqual(a.load_from_json_pokemons(a_list), True)
        # self.assertEqual(a.load_from_json_pokemons('pokemon'), False)

    def test_load_from_json_agents(self):
        a = GraphAlgo()
        a_list = {}
        try:
            # take from agent json example in "client"
            a_list = {"Agents": [{"Agent": {"id": 0, "value": 0.0, "src": 0, "dest": 1, "speed": 1.0, "pos":"35.18753053591606,32.10378225882353,0.0"}}]}
            json_string = json.dumps(a_list)
            json_file = open("../data/agent.json", "w")
            json_file.write(json_string)
            json_file.close()
        except:
            print("Error")

        self.assertEqual(a.load_from_json_agents('agent.json'), False)

    def test_shortest_path(self):
        a = GraphAlgo()
        f = open('../data/A0')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.shortest_path(1, 0, 1), (1.8884659521433524, [1, 0]))
        self.assertEqual(a.shortest_path(1, 7), (7.5417591783049245, [1, 0, 10, 9, 8, 7]))
        f.close()

        f = open('../data/A3')
        a.load_from_json_graph(json.load(f))
        self.assertEqual(a.shortest_path(1, 0, 1), (1.260431259778731, [1, 0]))
        self.assertEqual(a.shortest_path(35, 39), (3.90121586527845, [35, 36, 37, 39]))
        self.assertEqual(a.shortest_path(15, 18), (4.552847333258418, [15, 14, 17, 18]))
        f.close()

if __name__ == '__main__':
    unittest.main()
