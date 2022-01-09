from Ex4.GraphInterface import GraphInterface


class GraphAlgoInterface:
    """This abstract class represents an interface of a graph."""

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """

    def load_from_json_graph(self, file_name: dict) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        raise NotImplementedError

    def shortest_path(self, id1: int, id2: int, speed: float = 1) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @param speed: The speed of agent
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    def distance(self, pos, pos1) -> float:
        """return distance between two pos"""
        raise NotImplementedError

    def length_point_x(self, x1: float, x2: float) -> float:
        """return length point of x"""
        raise NotImplementedError

    def length_point_y(self, y1: float, y2: float) -> float:
        """return length point of y"""
        raise NotImplementedError

    def length_between2_segment(self, x1: float, x2: float) -> float:
        """return length between 2 segment, length of edge"""
        raise NotImplementedError

    def where_pokemon(self, pos: str) -> (int, int):
        """get pos of pokemon and return the src and dest, between which node is the pokemon"""
        raise NotImplementedError

    def when_get_to_pokemons(self, pos_pokemon, pos_l, pos_l2) -> int:
        """At what point the pokemon is on the node, a percentage relative to the node"""
        raise NotImplementedError

    def contains(self, pos: str, pos1: str, pos2: str):
        raise NotImplementedError

    def load_from_json_pokemons(self, data: dict):
        """Loads a pokemons from a json file."""
        raise NotImplementedError

    def load_from_json_agents(self, data: dict):
        """Loads a agents from a json file."""
        raise NotImplementedError

    def pokemon_selection_for_agent(self, id_a: int, id1: int, speed: float) -> (list, list, list):
        """Choose a Pokemon for the agent
        The algorithm checks which Pokemon is "best" for the agent to capture
        so that there will be no 2 agents approaching the same Pokemon.
        "Best" takes into account the shortest_path and also the value of all the Pokemon that are on the edge
        Detailed explanation of the algorithm in readme
        return shortest_path, list_stop, list_pos_to
        shortest_path -> Agent's route to get to Pokemon
        list_stop -> List of times to make a move
        list_pos_to -> List of pos move
        """
        raise NotImplementedError

