# OOP_Ex4_python

## Rules of the Game:
We are given a certain number of agents and Pokemon at the beginning of the game and we are given a directed and weighted graph that represents a map of a particular geographical area.
The Pokemon are set in our game to be diamonds. There are 2 different colors of diamonds: a pink color represented a diamond that is on an ascending side, and a white color that represents a diamond that is on a descending side.
At the beginning of the game the agents will be placed on the vertices of the graph and the diamonds will be placed on the edges of the graph.
Each diamond has a weight - how much is it value.
And each side of the graph also has a weight - which represents how long it takes to go through the side.
In addition, each agent has a different speed. Once an agent reaches a certain number of points his speed increases.
The goal of the agents is to catch as many diamonds as possible in the allotted time (between 30 and 120 seconds), as soon as an agent catch a diamond a new diamond appears elsewhere and so he continues to catch diamonds until the end of time. The higher the value of the diamond (its weight) the greater the total score at the end of the game.
The goal of the game is to finish with the highest possible score.

## Assumptions:
•	The graph is connected.
•	The game graph will contain a maximum of 200 vertices (so that we can see how the agents work and run the game).
•	The diamonds will always be on edge.
•	To capture a diamond should be in the right direction of the edge. If the diamond is ascending it should be captured on the ascending side and vice versa.
•	In addition, to capture a diamond one has to go through the vertices of its edge, it is impossible to "jump" to it.


## How the algorithm works:
•	Initial position of agents: There will be a sorted list that will represent the value of the diamonds. If there is one agent he will be placed next to the most expensive diamond, if there are 2 agents they will be placed next to the 2 most expensive diamonds according to the list and so on ..
•	How to assign diamonds to agents: Each agent will go for a diamond for which the path is the shortest and most cost-effective. That is, for each agent (source) we compare the shortest path to each edge on which a diamond (dest) is, the function will return the time, the agent's stops to the diamond, the value of the diamond on the tested edge (if there is more than one diamond on the edge,  will return the value of All), and a list of vertices through which the agent must pass to reach the rib. Once a diamond has been assigned to an agent we will mark it so that the other agents will not consider the way to it and will not choose to go for that diamond.
•	Once the agent reaches the first vertex of the selected edge he will again do a calculation of the time up to the diamond on the side and the time up to the opposite vertex.
•	Each time an agent captures a diamond, he will complete the transition on the rib, meaning he will move to the vertex on the other side and then he will recalculate which diamond he should go for.
•	The number of moves the program will make will not exceed 10 moves per second.

## class and “interfaces”: (python)
### GraphInterface  - This abstract class represents an interface of a graph.
•	v_size(self): Returns the number of vertices in this graph.
•	e_size(self): Returns the number of edges in this graph.       
•	get_all_v(self):  return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).
•	all_in_edges_of_node(self, id1: int): return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight).
•	all_out_edges_of_node(self, id1: int): return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight).
•	add_edge(self, id1: int, id2: int, weight: float):  Adds an edge to the graph.   
(id1: The start node of the edge, id2: The end node of the edge, weight: The weight of the edge) . return true if the edge was added successfully, False o.w.
•	add_node(self,  node_id: int, pos: tuple = None):   Adds a node to the graph. (node_id: The node ID, pos: The position of the node). 
return true if the node was added successfully, False o.w.
•	remove_node(self, node_id: int):  Removes a node from the graph. return true if the node was removed successfully, False o.w.
•	remove_edge(self, node_id1: int, node_id2: int): return true if the edge was removed successfully, False o.w.
•	get_all_pokemons – return all pokemons in the graph.
•	pokemons_size(self) - Returns the number of pokemons in this graph
•	sort_pokemon_value – sort pokemons by there values, to know at what point it is best for an agent to start
•	get_all_agents – get agents that play on the graph.
•	get_all_pokemons_add(self) - return a dictionary of all the pokemons in the Graph connected from src node id , each pokemon is represented using a pair (dest node id, list value of pokemons in edge)
•	get_all_pokemons_pos(self) - return a dictionary of all the pokemons in the Graph connected from src node id , each pokemon is represented using a pair(dest node id, list pos of pokemons in edge)            
•	get_node_x(self, id: int) - return the x number of the node position 
•	get_node_y(self, id: int) - return the y number of the node position
•	agents_pos(self, id, pos) - update 'pos_do' of agent, 'pos_do' indicates the pos of the Pokemon he is on his way to 'pos_do' - parameter created to help to know which Pokemon each agent is targeting,  so there will be no 2 agents moving to the same Pokemon.
•	get_x_y(self, pos: str) - the x,y numbers of the pos position
•	get_node_pos(self, id: int) - return node pos get id
•	add_pokemon(self, count11: str, value11: float, image11: str, pos11: str, src11: int, dest11: int, type11: int):  Adds a pokimon to the graph.
Add the Pokemon information to 3 different data structures
•	add_agents(self, id: int, value: float, src: int, dest: int, speed: float, pos: str, grade: int = 0)-Add the agents information - The relevant information that get from json in addition to that pos_do -  parameter created to help to know which Pokemon each agent is targeting, so there will be no 2 agents moving to the same Pokemon.
•	remove_all_pokemons(self)-  all pokemons from data structures pokemons
•	remove_all_pokemons_add(self)-Removes all pokemons from data structures pokemons_add,pokemons_pos
•	 remove_all_agents(self)- Removes all agents from data structures agents

### DiGraph -  Implementing an Interface GraphInterface.
Data structures in digraph- node_list: dict, in_edge: dict, out_edge: dict, pokemons: dict, pokemons_add: dict, pokemons_pos: dict, agents: dict.
pokemons - The relevant information that get from json, in addition to that:
   src and dest The information obtained from the calculation to know between which sides is the Pokemon,
   image To know which image to place as a Pokemon (a silver diamond indicates a type smaller than 0, a pink diamond indicates a type larger than 0)
pokemons_add - the pokemons connected from src node id , each pokemon is represented using a pair (dest node id, list value of pokemons in edge)
pokemons_pos - the pokemons in the Graph connected from src node id , each pokemon is represented using a pair(dest node id, list pos of pokemons in edge)
•	The agent data structure contains, among other things, that pos_do -  parameter created to help to know which Pokemon each agent is targeting, so there will be no 2 agents moving to the same Pokemon.

### GraphAlgoInterface  - This abstract class represents an interface of a graph.
•	get_graph(self)-  return: the directed graph on which the algorithm works on.
•	load_from_json_graph(self, file_name: dict) -Loads a graph from a json file.
•	shortest_path(self, id1: int, id2: int, speed: float = 1) -nReturns the shortest path from node id1 to node id2 using Dijkstra's Algorithm. The distance of the path, a list of the nodes ids that the path goes through, Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
•	distance(self, pos, pos1) - return distance between two pos
•	length_point_x(self, x1: float, x2: float) - return length point of x
•	length_point_y(self, y1: float, y2: float) - return length point of Y
•	length_between2_segment(self, x1: float, x2: float) -return length between 2 segment, length of edge
•	where_pokemon(self, pos: str) - get pos of pokemon and return the src and dest, between which node is the pokemon
•	when_get_to_pokemons(self, pos_pokemon, pos_l, pos_l2) - At what point the pokemon is on the node, a percentage relative to the node
•	load_from_json_pokemons(self, data: dict-Loads a pokemons from a json file.
•	load_from_json_agents(self, data: dict)- Loads a agents from a json file
•	pokemon_selection_for_agent(self, id_a: int, id1: int, speed: float) - Choose a Pokemon for the agent The algorithm checks which Pokemon is "best" for the agent to capture so that there will be no 2 agents approaching the same Pokemon. "Best" takes into account the shortest_path and also the value of all the Pokemon that are on the edge Detailed explanation of the algorithm in readme. return shortest_path, list_stop, list_pos_to
        shortest_path -> Agent's route to get to Pokemon
        list_stop -> List of times to make a move
        list_pos_to -> List of pos move
        

### GraphAlgo – Implementing an Interface GraphAlgoInterface.

### GraphView:  Creates a drawing of a graph. The details shown in the graph: how much time is left, the score of each agent, the agents (the amount of agents is given according to the different json that runs), the Pokemon (the amount of the pixons and their location is given by Client).

### Main – use to check our GraphView. 
Given class -client:
•	start_connection - start a new connection to the game server.
•	getAgents - Returns the agents
•	add_agent - adds agent
•	getGraph - Returns the graph
•	getInfo - gives all the information at the end of the game, gives a score, some agents… Starts at the beginning of the game with the amount of agents and more information that is used in the program
•	getPokemons - Returns information about Pokemon (value, ascending / descending side, and location), array of Pokemon
•	isRunnig - Returns true if already started otherwise will return false
•	time_to_end - returns time to end in mili-seconds str.
•	start - use start to run the game
•	stop - use stop to end the game and upload results.
•	move - activate all valid choose_next_edge calls. returns: agents state with the same form as get_agents ().
•	choose_next_edge - choosing the next destination for a specific agent. 1. the agent is still moving on some edge, (ak agent.dest! = -1) or 2. the "next_node_id" isn't an adjacent vertex of agent.src, then move () will not be affected by this invalid "next_node_id" choice. 
TestDiGraph: test class DiGraph.
TestGraphAlgo: test class GraphAlgo.


### How to download, run and use the graphical interface:
•	To run the gui run you need to call the class ie: "GraphView ()"
•	The updated information is indicated at the top
•	There is a stop button at the top right

### Import libraries:
Pygame


![video_git](https://user-images.githubusercontent.com/93534494/148702620-9a275f0b-0792-4b5d-b1ea-603198958bc6.gif)





