import sys
import math
import numpy as np
from Ex4.DiGraph import DiGraph
from Ex4.GraphAlgoInterface import GraphAlgoInterface
from Ex4.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, di_graph: DiGraph = DiGraph()):
        self.di_graph = di_graph

    def get_graph(self) -> GraphInterface:
        return self.di_graph

    def load_from_json_graph(self, file_name: dict) -> bool:
        self.di_graph = DiGraph()
        try:
            data = file_name
            for i in data['Nodes']:
                if "pos" in i:
                    self.di_graph.add_node(i["id"], i["pos"])
                else:
                    self.di_graph.add_node(i["id"])
            for i in data['Edges']:
                self.di_graph.add_edge(i["src"], i["dest"], i["w"])
            return True
        except IOError:
            return False
        except:
            return False

    def distance(self, pos, pos1) -> float:
        poss = pos.split(",")
        poss1 = pos1.split(",")
        dx = float(poss[0]) - float(poss1[0])
        dy = float(poss[1]) - float(poss1[1])
        t = (dx * dx + dy * dy)
        if t < 0:
            return 0
        return math.sqrt(t)

    def length_point_x(self, x1: float, x2: float) -> float:
        return self.length_between2_segment(x1, x2)

    def length_point_y(self, y1: float, y2: float) -> float:
        return self.length_between2_segment(y1, y2)

    def length_between2_segment(self, x1: float, x2: float) -> float:
        divideByDozens = (len(str(x1)) - (str(x1)).index(".") - 1) * 10
        x1 *= divideByDozens
        divideByDozensY = (len(str(x2)) - ((str(x2)).index(".")) - 1) * 10
        x2 *= divideByDozensY
        if divideByDozens > divideByDozensY:
            x2 *= divideByDozens / divideByDozensY
        else:
            if divideByDozens < divideByDozensY:
                x1 *= divideByDozensY / divideByDozens
                divideByDozens = divideByDozensY
        if divideByDozens == 0:
            divideByDozens = 1
        return ((abs(x1 - x2)) / divideByDozens)

    def where_pokemon(self, pos: str) -> (int, int):
        exact_distance = sys.float_info.max
        src = -1
        dest = -1
        EPS = np.finfo(float).eps
        for i in self.di_graph.get_all_v():
            for j in self.di_graph.all_out_edges_of_node(i):
                pos1 = self.di_graph.get_all_v()[i]
                pos2 = self.di_graph.get_all_v()[j]
                num = self.contains(pos, pos1, pos2)
                if num < 100 * EPS:
                    src = i
                    dest = j
                    return src, dest
                if exact_distance > num:
                    exact_distance = num
                    src = i
                    dest = j
        return src, dest

    def when_get_to_pokemons(self, pos_pokemon, pos_l, pos_l2) -> int:
        distOtToP1 = self.distance(pos_l, pos_pokemon)
        distOtToP2 = self.distance(pos_l, pos_l2)
        t = int(distOtToP1/(distOtToP2/100))
        return t

    def contains(self, pos: str, pos1: str, pos2: str):
        distOtToP1 = self.distance(pos, pos1)
        distOtToP2 = self.distance(pos, pos2)
        poss1 = pos2.split(",")
        poss = pos1.split(",")
        lengthSegment = math.sqrt(self.length_point_x(float(poss[0]), float(poss1[0])) *
                                  self.length_point_x(float(poss[0]), float(poss1[0])) +
                                  self.length_point_y(float(poss[1]), float(poss1[1])) *
                                  self.length_point_y(float(poss[1]), float(poss1[1])))
        return distOtToP1 + distOtToP2 - lengthSegment

    def load_from_json_pokemons(self, data: dict):
        self.di_graph.remove_all_pokemons()
        self.di_graph.remove_all_pokemons_add()
        try:
            count = 0
            for i in data['Pokemons']:
                p1, p2 = self.where_pokemon(i['Pokemon']['pos'])
                if i['Pokemon']['type'] < 0:
                    if p1 < p2:
                        dest = p1
                        src = p2
                    else:
                        dest = p2
                        src = p1
                    image = "diamondWhite"
                else:
                    if p1 < p2:
                        src = p1
                        dest = p2
                    else:
                        src = p2
                        dest = p1
                    image = "diamondPink"
                self.di_graph.add_pokemon(i['Pokemon']['pos'], i['Pokemon']['value'], image, i['Pokemon']['pos'],
                                          src, dest, i['Pokemon']['type'])
                count += 1
            return True
        except IOError:
            return False
        except:
            return False

    def load_from_json_agents(self, data: dict):
        try:
            for i in data['Agents']:
                self.di_graph.add_agents(i['Agent']["id"], i['Agent']["value"], i['Agent']["src"],
                                         i['Agent']["dest"], i['Agent']["speed"], i['Agent']["pos"])
            return True
        except IOError:
            return False
        except:
            return False

    def shortest_path(self, id1: int, id2: int, speed: float = 1) -> (float, list):
        nodes = list(self.di_graph.get_all_v())
        distance_path, pre_node = {}, {}
        for node in nodes:
            distance_path[node] = sys.maxsize
        distance_path[id1] = 0
        while nodes:
            node_m = None
            for node in nodes:
                if node_m is None:
                    node_m = node
                elif distance_path[node] < distance_path[node_m]:
                    node_m = node
            out_edges = self.di_graph.all_out_edges_of_node(node_m)
            for edge in out_edges:
                distance = distance_path[node_m] + (self.di_graph.all_out_edges_of_node(node_m)[edge] / speed)
                if distance < distance_path[edge]:
                    distance_path[edge] = distance
                    pre_node[edge] = node_m
            nodes.remove(node_m)
        end_path = id2
        shortest_path = [end_path]
        while end_path != id1:
            if end_path not in pre_node:
                return math.inf, []
            shortest_path.append(pre_node[end_path])
            end_path = pre_node[end_path]
        shortest_path.reverse()
        return distance_path[id2], shortest_path

    def pokemon_selection_for_agent(self, id_a: int, id1: int, speed: float) -> (list, list, list):
        nodes = self.di_graph.get_all_v()
        pokemons = self.di_graph.get_all_pokemons_add()
        pokemons_pos = self.di_graph.pokemons_pos
        agents = self.di_graph.get_all_agents()
        pos_agent = ''
        pokemons_info = self.di_graph.get_all_pokemons()
        if len(pokemons) == 0:
            return [], [], []
        fa = list(pokemons.keys())[0]
        i = 1
        test2 = True
        while test2 and i >= len(list(pokemons.keys())):
            test = False
            for de in pokemons_pos[fa]:
                lis_pos_1 = pokemons_pos[fa][de]
                for ir in lis_pos_1:
                    for agent1_a in agents:
                        if agents[agent1_a]['pos_do'] != '' and agents[agent1_a]['pos_do'] == ir and agent1_a != id_a:
                            test = True
            if test:
                fa = list(pokemons.keys())[i]
                i += 1
            else:
                test2 = False
        sum_max = 0.0
        dest = 0
        for dest_i in pokemons[fa]:
            values = pokemons[fa][dest_i]
            sum = 0.0
            for i in range(len(values)):
                sum += values[i]
            if sum_max < sum:
                sum_max = sum
                dest = dest_i
        distance, shortest_path = self.shortest_path(id1, fa, speed)
        shortest_path.append(dest)
        if distance == 0:
            pos_l = nodes[fa]
            pos_d = nodes[dest]
            list_stop = []
            pok1_max = 0
            pos_pos = 0
            lisy_pos_to = []
            for i in pokemons_info:
                if pokemons_info[i]['src'] == fa and pokemons_info[i]['dest'] == dest:
                    if pos_agent != '':
                        pok_src = self.when_get_to_pokemons(pos_agent, pos_l, pos_d)
                    else:
                        pok_src = 0
                    pok1 = self.when_get_to_pokemons(i, pos_l, pos_d)
                    r = ((self.di_graph.all_out_edges_of_node(fa)[dest] * ((pok1-pok_src) / 100)) / speed)
                    pos_pos = i
                    lisy_pos_to.append(pos_pos)
                    list_stop.append(r)
                    if pok1_max < pok1:
                        pok1_max = pok1
            self.di_graph.agents_pos(id_a, pos_pos)
            list_stop = sorted(list_stop)
            r2 = ((self.di_graph.all_out_edges_of_node(fa)[dest] * ((100 - pok1_max) / 100)) / speed)
            for i in range(len(list_stop)-1):
                list_stop[len(list_stop)-i-1] = list_stop[len(list_stop)-i-1] - list_stop[len(list_stop)-i-2]
            list_stop.append(r2)
            lisy_pos_to.append(self.di_graph.get_node_pos(dest))
            return shortest_path, list_stop, lisy_pos_to
        values = pokemons[fa][dest]
        sum_value = 0.0
        for i in range(len(values)):
            sum_value += values[i]
        if distance == 0:
            comparison = 0
        else:
            comparison = sum_value / distance
        for p in pokemons:
            if p != fa:
                test = False
                for de in pokemons_pos[p]:
                    lis_pos_1 = pokemons_pos[p][de]
                    for ir in lis_pos_1:
                        for agent1_a in agents:
                            if agents[agent1_a]['pos_do'] != '' and agents[agent1_a]['pos_do'] == ir and agent1_a != id_a:
                                test = True
                if not test:
                    distance2, shortest_path1 = self.shortest_path(id1, p, speed)
                    key_dest = list(pokemons[p].keys())
                    all_values = list(pokemons[p].values())
                    dest = key_dest[all_values.index(max(all_values))]
                    shortest_path1.append(dest)
                    values = pokemons[p][dest]
                    value = 0.0
                    for i in range(len(values)):
                        value += values[i]
                    if sum_max < value:
                        sum_max = value
                    if (comparison * distance2) < value:
                        fa = p
                        if distance2 == 0:
                            pos_l = nodes[fa]
                            pos_d = nodes[dest]
                            pos_pos = 0
                            pok1_max = 0
                            list_stop = []
                            list_pos_to = []
                            for i in pokemons_info:
                                if pokemons_info[i]['src'] == fa and pokemons_info[i]['dest'] == dest:
                                    pok1 = self.when_get_to_pokemons(i, pos_l, pos_d)
                                    if pos_agent != '':
                                        pok_src = self.when_get_to_pokemons(pos_agent, pos_l, pos_d)
                                    else:
                                        pok_src = 0
                                    r = ((self.di_graph.all_out_edges_of_node(fa)[dest] * ((pok1 - pok_src) / 100)) / speed)
                                    pos_pos = i
                                    list_pos_to.append(pos_pos)
                                    list_stop.append(r)
                                    if pok1_max < pok1:
                                        pok1_max = pok1
                            self.di_graph.agents_pos(id_a, pos_pos)
                            list_stop = sorted(list_stop)
                            r2 = ((self.di_graph.all_out_edges_of_node(fa)[dest] * ((100 - pok1_max) / 100)) / speed)
                            for i in range(len(list_stop) - 1):
                                list_stop[len(list_stop) - i - 1] = list_stop[len(list_stop) - i - 1] - list_stop[
                                    len(list_stop) - i - 2]
                            list_stop.append(r2)
                            list_pos_to.append(self.di_graph.get_node_pos(dest))
                            return shortest_path1, list_stop, list_pos_to
                        key_dest = list(pokemons[fa].keys())
                        all_values = list(pokemons[fa].values())
                        dest = key_dest[all_values.index(max(all_values))]
                        values = pokemons[fa][dest]
                        sum_value = 0.0
                        for i in range(len(values)):
                            sum_value += values[i]
                        if distance2 == 0:
                            comparison = 0
                        else:
                            comparison = sum_value / distance2
        distance, shortest_path = self.shortest_path(id1, fa, speed)
        key_dest = list(pokemons[fa].keys())
        all_values = list(pokemons[fa].values())
        dest = key_dest[all_values.index(max(all_values))]
        shortest_path.append(dest)
        r = 0
        lis_pos = pokemons_pos[fa][dest]
        pos_pos = lis_pos[0]
        self.di_graph.agents_pos(id_a, pos_pos)
        for i in pokemons_info:
            if pokemons_info[i]['src'] == fa and pokemons_info[i]['dest'] == dest:
                r = ((self.di_graph.all_out_edges_of_node(shortest_path[0])[shortest_path[1]] * (100 / 100)) / speed)
        list_stop = [r, 0]
        list_pos_to = [self.di_graph.get_node_pos(shortest_path[1])]
        return shortest_path, list_stop, list_pos_to
