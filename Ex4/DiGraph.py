from Ex4.GraphInterface import GraphInterface
import random


class DiGraph(GraphInterface):
    def __init__(self):
        self.node_list: dict = {}
        self.in_edges: dict = {}
        self.out_edges: dict = {}
        self.pokemons: dict = {}
        self.pokemons_add: dict = {}
        self.pokemons_pos: dict = {}
        self.agents: dict = {}

    def v_size(self) -> int:
        return len(self.node_list)

    def pokemons_size(self) -> int:
        return len(self.pokemons)

    def e_size(self) -> int:
        size_edge = 0
        for node in self.node_list:
            size_edge += len(self.all_out_edges_of_node(node))
        return size_edge

    def get_node_pos(self, id: int) -> str:
        return self.node_list[id]

    def get_node_x(self, id: int) -> float:
        pos = self.node_list[id].split(",")
        return pos[0]

    def get_node_y(self, id: int) -> float:
        pos = self.node_list[id].split(",")
        return float(pos[1])

    def get_node_x(self, id: int) -> float:
        pos = self.node_list[id].split(",")
        return float(pos[0])

    def get_all_v(self) -> dict:
        return self.node_list

    def get_all_pokemons(self) -> dict:
        return self.pokemons

    def get_all_pokemons_add(self) -> dict:
        return self.pokemons_add

    def get_all_pokemons_pos(self) -> dict:
        return self.pokemons_pos

    def sort_pokemon_value(self) -> list:
        sort_p = list(reversed(sorted(self.pokemons.keys(), key=lambda x: self.pokemons[x]['value'])))
        return sort_p

    def get_all_agents(self) -> dict:
        return self.agents

    def get_x_y(self, pos: str) -> (float, float):
        pos = pos.split(",")
        return float(pos[0]), float(pos[1])

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.in_edges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.out_edges.get(id1)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        if (id2 in self.node_list) and (id1 in self.node_list):
            if id2 not in self.out_edges[id1]:
                self.out_edges[id1].update({id2: weight})
                self.in_edges[id2].update({id1: weight})
                return True
        return False

    def add_pokemon(self, count11: str, value11: float, image11: str, pos11: str, src11: int, dest11: int, type11: int):
        if count11 not in self.pokemons:
            if src11 in self.pokemons_pos:
                if dest11 in self.pokemons_pos[src11]:
                    list_value = self.pokemons_add[src11][dest11]
                    list_value.append(value11)
                    self.pokemons_add[src11][dest11] = list_value
                    list_pos = self.pokemons_pos[src11][dest11]
                    list_pos.append(pos11)
                    self.pokemons_pos[src11][dest11] = list_pos
                else:
                    self.pokemons_pos[src11] = ({dest11: [pos11]})
                    self.pokemons_add[src11] = ({dest11: [value11]})
            else:
                self.pokemons_pos[src11] = ({dest11: [pos11]})
                self.pokemons_add[src11] = ({dest11: [value11]})
            self.pokemons[count11] = ({"value": value11, "image": image11, "pos": pos11, "src": src11, "dest": dest11,
                                       "type": type11})
        else:
            self.pokemons[count11].update({"value": value11, "image": image11, "pos": pos11, "src": src11,
                                           "dest": dest11, "type": type11})
        return True

    def agents_pos(self, id, pos):
        self.agents[id].update({"pos_do": pos})

    def add_agents(self, id: int, value: float, src: int, dest: int, speed: float, pos: str, grade: int = 0):
        if id in self.agents:
            self.agents[id].update({"id": id, "value": value, "src": src, "dest": dest, "speed": speed, "pos": pos})
            return True
        self.agents[id] = {"id": id, "value": value, "src": src, "dest": dest, "speed": speed, "pos": pos,
                           "grade": grade, "pos_do": ""}
        return True

    def remove_all_pokemons(self):
        self.pokemons: dict = {}

    def remove_all_pokemons_add(self):
        self.pokemons_add: dict = {}
        self.pokemons_pos: dict = {}

    def remove_all_agents(self):
        self.agents: dict = {}

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos is None:
            pos = str(35 + random.random()) + ',' + str(32 + random.random()) + ',0.0'
        if node_id not in self.node_list:
            self.node_list[node_id] = pos
            self.in_edges[node_id] = {}
            self.out_edges[node_id] = {}
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.node_list is None:
            return False
        if self.out_edges is None:
            return False
        if self.in_edges is None:
            return False
        for x in self.node_list:
            self.remove_edge(node_id, x)
            self.remove_edge(x, node_id)
        if node_id not in self.node_list:
            return False
        node_data = self.node_list[node_id]
        if node_data is not None:
            self.node_list.pop(node_id)
            if self.in_edges is not None:
                self.in_edges.pop(node_id)
            if self.out_edges is not None:
                self.out_edges.pop(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.in_edges is None:
            return False
        if self.out_edges is None:
            return False
        if node_id1 not in self.out_edges:
            return False
        if self.out_edges[node_id1] is None:
            return False
        if node_id2 not in self.in_edges:
            return False
        if self.in_edges[node_id2] is None:
            return False
        if node_id2 in self.out_edges[node_id1]:
            self.out_edges[node_id1].pop(node_id2)
            self.in_edges[node_id2].pop(node_id1)
            return True
        return False

    def __str__(self):
        list_e = {"Edges": [], "Nodes": []}
        list_e["Nodes"].append(self.node_list)
        for node in self.node_list:
            list_out = self.all_out_edges_of_node(node)
            for x in list_out:
                list_e["Edges"].append({x, node, list_out[x]})
        return str(list_e)
