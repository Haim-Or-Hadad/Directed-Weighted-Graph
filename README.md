 # Exercise 3 | Directed Weighted Graph 
 ## Introduction
 This project is dedicated for planning and implement of a Directed Weight Graphs with data sturctures in Python. <br/>
Graph is a structure with sets of nodes and edges. when the nodes are objects on the space and the edges <br/>
are connecting between them .<br/>
In this task we need to get files that contains list of vertexs and edges and build object(DiGrpah) for them. <br/>
Then we use the graph for testing and running diffrent algorithms .
In addition the project includes a GUI that use in pygame that draws graph on the screen and run diffrent functions 
on him. <br/>
## UML
UML is a general-purpose, developmental, modeling language in the field of software
engineering that is intended to provide a standard way to visualize the design of a system.
In this UML we are planning how the project will look like. <br/>
<img src="https://user-images.githubusercontent.com/93033782/147382525-ed711383-c9ef-4b92-88f2-72eec7ce0700.jpeg" width="600"> <br/>
## src 
### Node
Node this class that represents  set of operations applicable on a node (vertex) in a (directional) weighted graph.<br/>
 ***new fields:*** <br/>
- private tuple pos - position of the node.
- private int id - the key that will be useful for the structure of graph.
- private double weight- the weight of the node for the algorithm.
- private String Info.
- private int Tag- useful for the algorithms.
- private connect_out - dict that save all vertexts the go out from specific node.
- private connect_int - dict that save all vertexts the go in to specific node.
-  private max_weight - save the max weight of path for the algorithm.    <br/>

 Methods       | Performs | Complexity time 
--------------------------|----------------------|--------
__init__ | counstructor of a new Node | O(1)
x     | return value of pos.x | O(1)
y      | return value of pos.y | O(1)
get_id      | return the id of tha node | O(1)
get_pos                  | return the position of the node | O(1)
get_tag             | return the tag of the node | O(1)
get_out| all the nodes that this node connect them | O(1)
get_in                | all the edges that arrived to this node | O(1)
add_connect_out       | add edge between this node to neighbor node | O(1)
add_connect_in           | add edge that connect to this node | O(1)
__str__         | print the node | O(1)
__repr__                  | print the node | O(1)  <br/>
### DiGraph
DiGraph this class that build the new graph . By use in nodes  we build a new structure that represent the new graph. <br/>
The class implement the interface **GraphInterface**, This interface represents a Directional Weighted Graph <br/>
The interface has a road-system or communication network in mind - and should support a large number of nodes . our implemention <br/>
based on an two dictionary that save all the edges in the graph. <br/>
***New Fields*** <br/>
- nodes -> dict()
- num_of_edge -> int
- mc -> int <br/>

 Methods       | Performs | Complexity
--------------------------|-----------------------------------------|---------
__init__ | create a new object of graph | O(1)
v_size| return the number of nodes in graph |O(1)
e_size               | return the number of edges in graph |O(1)
get_all_v     | return a dictionary of all the nodes in the Graph |O(1)
all_in_edges_of_node(id1: int)           | return all the nodes that enter to the node |O(1)
all_out_edges_of_node(id1: int)  | Return all the nodes that go out from node |O(1)
get_mc                            |Returns the current version of this graph | O(1)
add_edge(id1: int, id2: int, weight: float)                    | Adds an edge to the graph  | O(1)
add_node(node_id: int, pos: tuple = None)         | Adds a node to the graph | O(1)
remove_node(node_id: int)           |  Removes a node from the graph  | O(n)
removeEdge(node id1 :int  , node id2: int) |  Removes an edge from the graph| O(1)
__repr__ |  print method | O(1)  <br/>

### GraphAlgo
GraphAlgo is class that run algorithms on the graph. the class implement the interface **GraphAlgoInteface**.<br/>
This interface represents a Directed (positive) Weighted Graph Theory Algorithms that includes 6 algorithms. <br/>


 Methods       | Performs | Complexity
--------------------------|-----------------------------------------|---------
__init__ | create a new object of graph | O(1)
get_graph| return the number of nodes in graph | O(1)
load_from_json(file_name: str)               | Loads a graph from a json file | O(n) or O(e)
save_to_json     | Saves the graph in JSON format to a file |O(n) or O(e)
shortest_path(id1: int, id2: int)           | Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm | ?
TSP(self, node_lst: List[int])  | Finds the shortest path that visits all the nodes in the list | ?
centerPoint               |Finds the node that has the shortest distance to it's farthest node | ?
plot_graph                    | Plots the graph  | ?   <br/>

### Elaboration
- load_from_json - this algorithm Loads a graph from a json file . firstly we run over all the nodes in add them to the graph <br/>
and after this we add all edges to graph , so if there are more edges than nodes the run time complexity is O(e), otherwise <br/>
it's O(n) <br/>
- save_to_json - this algorithm Saves the graph in JSON format to a file . the time complexity is the same like load function <br/>
from the same reasons. <br/>
-shortest_path - <br/>
-TSP-  <br/>
-centerPoint-   <br/>
-plot_graph <br/>

