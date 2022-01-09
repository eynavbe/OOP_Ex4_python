class GraphInterface:
    """This abstract class represents an interface of a graph."""

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        raise NotImplementedError

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        raise NotImplementedError

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        raise NotImplementedError

    def get_all_pokemons(self) -> dict:
        """return a dictionary of all the pokemons in the Graph
                """
        raise NotImplementedError

    def pokemons_size(self) -> int:
        """Returns the number of pokemons in this graph"""
        raise NotImplementedError

    def sort_pokemon_value(self) ->list:
        """Sort the pokemon by their value.
        to know at what point it is best for an agent to start"""
        raise NotImplementedError

    def get_all_agents(self) -> dict:
        """return a dictionary of all the agents in the Graph
                        """
        raise NotImplementedError

    def get_all_pokemons_add(self) -> dict:
        """return a dictionary of all the pokemons in the Graph connected from src node id , each pokemon is represented using a pair
               (dest node id, list value of pokemons in edge)
               """
        raise NotImplementedError

    def get_all_pokemons_pos(self) -> dict:
        """return a dictionary of all the pokemons in the Graph connected from src node id , each pokemon is represented using a pair
                       (dest node id, list pos of pokemons in edge)
                       """
        raise NotImplementedError

    def get_node_x(self, id: int) -> float:
        """return the x number of the node position"""
        raise NotImplementedError

    def get_node_y(self, id: int) -> float:
        """return the y number of the node position"""
        raise NotImplementedError

    # def add_node(self, node_id: int, x: int, y: int) -> bool:

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        raise NotImplementedError

    def agents_pos(self, id, pos):
        """update 'pos_do' of agent, 'pos_do' indicates the pos of the Pokemon he is on his way to
        'pos_do' - parameter created to help to know which Pokemon each agent is targeting,
         so there will be no 2 agents moving to the same Pokemon.
        """
        raise NotImplementedError

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError

    def get_x_y(self, pos: str) -> (float, float):
        """return the x,y numbers of the pos position"""
        raise NotImplementedError

    def get_node_pos(self, id: int) -> str:
        """return node pos get id"""
        raise NotImplementedError

    def add_pokemon(self, count11: str, value11: float, image11: str, pos11: str, src11: int, dest11: int, type11: int):
        """Adds a pokimon to the graph.
        Add the Pokemon information to 3 different data structures
        pokemons - The relevant information that get from json, in addition to that:
                src and dest The information obtained from the calculation to know between which sides is the Pokemon,
                image To know which image to place as a Pokemon (a silver diamond indicates a type smaller than 0,
                a pink diamond indicates a type larger than 0)
        pokemons_add - the pokemons connected from src node id , each pokemon is represented using a pair
               (dest node id, list value of pokemons in edge)
        pokemons_pos - the pokemons in the Graph connected from src node id , each pokemon is represented using a pair
                       (dest node id, list pos of pokemons in edge)
        """
        raise NotImplementedError

    def add_agents(self, id: int, value: float, src: int, dest: int, speed: float, pos: str, grade: int = 0):
        """Add the agents information - The relevant information that get from json
            in addition to that pos_do -  parameter created to help to know which Pokemon each agent is targeting,
         so there will be no 2 agents moving to the same Pokemon.
        """
        raise NotImplementedError

    def remove_all_pokemons(self):
        """Removes all pokemons from data structures pokemons"""
        raise NotImplementedError

    def remove_all_pokemons_add(self):
        """Removes all pokemons from data structures pokemons_add,pokemons_pos"""
        raise NotImplementedError

    def remove_all_agents(self):
        """Removes all agents from data structures agents"""
        raise NotImplementedError

