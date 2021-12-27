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
-  private max_weight - save distance of the current node to it's farthest node in the garph.    <br/>

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
load_from_json(file_name: str)               | Loads a graph from a json file | O(n+e)
save_to_json     | Saves the graph in JSON format to a file |O(n*e)
shortest_path(id1: int, id2: int)           | Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm | O(e + n*log n)
TSP(self, node_lst: List[int])  | Finds the shortest path that visits all the nodes in the list | O(n!*(e + n*log n))
centerPoint               |Finds the node that has the shortest distance to it's farthest node | O(n(e + n*log n))
plot_graph                    | Plots the graph  | ?   
dijkstra(src: int)           | Find the distance from src node to all the nodes in the graph | O(e + n*log n)<br/>

### Elaboration
- <b>load_from_json</b> - This algorithm Loads a graph from a json file . firstly we run over all the nodes in the json file and add them to the graph <br/>
and after this we add all edges to graph , so if there are more edges than nodes the run time complexity is O(e), otherwise <br/>
it's O(n) <br/>
- <b>save_to_json</b> - This algorithm Saves the graph in JSON format to a file . the function go over the nodes and for each node it save all the edges going out of the node. <br/> <br/>
- <b>shortest_path</b> - Shortest path funtion active dijkstra algorithm for the id1 node and find the shortest path according to the results <br/>
- <b>TSP</b> - Tsp create a list with all the possible permutations, after that the function run over each permutations take the first node in the list activate a dijkstra algorithm once and sum the distances for each node in the list.   <br/>
- <b>centerPoint</b> - Center point run dijkstra algorithm on each node and update the max weight that save the distance to the farthest node, after that it run over all the nodes and return the  node that has the shortest distance of all the max weight in the graph.       <br/>
- <b>plot_graph</b> - <br/>

## Instrucion
**instrucion for using the graphical interface** <br/>
<img src="https://user-images.githubusercontent.com/93033782/147508188-cd479101-391e-4007-84ae-5c57180a137d.png" width="600"> <br/>
### save
<img src="https://user-images.githubusercontent.com/93033782/147509287-797b9dcd-b6e2-46f0-8b9d-ba1492c45fb3.png" width="100"> <br/>
click on save button and a text box pop up <br/>
<img src="https://user-images.githubusercontent.com/93033782/147509375-2b5f54ae-b6d7-41ea-971a-9804b0f3256d.png" width="350"> <br/>
enter please new file name that you want and click "ok". <br/>
### load
<img src="https://user-images.githubusercontent.com/93033782/147509534-11597093-3434-4ee0-8cd3-0937cd1c776c.png" width="100"> <br/>
click on load button and a file chooser pop up <br/>
<img src="https://user-images.githubusercontent.com/93033782/147509631-d55f5e4f-b422-4e77-8a50-531e86e0ad3e.png" width="350"> <br/>
please click on the graph that you want to load <br/>
### TSP
<img src="https://user-images.githubusercontent.com/93033782/147509810-083c36c3-dc96-4d86-9074-fe2924e7c761.png" width="100"> <br/>
click on the TSP button and a file chooser pop up <br/>
<img src="https://user-images.githubusercontent.com/93033782/147509968-c206512d-eb27-4b7f-b61c-897f317839d8.png" width="350"> <br/>
like in the picture please enter numbers with comma between them. <br/>
when you click ok the window will show you the answer. <br/>
### s-path
<img src="https://user-images.githubusercontent.com/93033782/147510394-bb6327fd-f6b2-4874-a2a0-ec7d17a864f1.png" width="100"> <br/>
click on s-path button and this text box pop up <br/>
<img src="https://user-images.githubusercontent.com/93033782/147510177-d6e6c343-c500-4461-a4bf-04822277d927.png" width="350"> <br/>
please enter here the source id node <br/>
<img src="https://user-images.githubusercontent.com/93033782/147510240-bcfe68c8-c53e-4509-81a2-1456211897e4.png" width="350"> <br/>
please enter here the dest id node <br/>
### center
<img src="https://user-images.githubusercontent.com/93033782/147510456-4fc63d36-082b-4b72-b058-00cbc076d56e.png" width="100"> <br/>
click on center button and the center node will marked for a second , please click again if you dont see. <br/>
<img src="https://user-images.githubusercontent.com/93033782/147510600-cddb8cb2-7d6d-427a-bae7-79b0afda40d0.png" width="350"> <br/>
### add edge/node remove edge/node buttons
<img src="https://user-images.githubusercontent.com/93033782/147510939-b837f870-2688-4baa-810a-c55fb2b35a49.png" width="350"> <br/>
click on the operation that you want to do and enter the id of the node that you want to add or remove.<br/>
if you click on edge operation please enter also dest id . <br/>

## Performes of largh graphs:
   Graph        | load_from_json | save | s-Path | center
-----------------|-----------|------------------------|---------------|--------------------
1000Nodes        | 0.0263 ms      |0.123 ms  |    (55,721) 10.88 sec|list=(7,27,734,888,576) 57ms   
10000Nodes       | 0.282 ms |1.4037 sec |        (55,5000) 1 sec 27 ms | list=(7,1000,3301,7555,9999) 1 sec 
100000Nodes       | 5.829 sec |26.626 sec|      16 sec 92 ms | list=(76,1060,33601,75565,99998) 1 minute 10 ms   






