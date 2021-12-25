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
 ***new fields:***
 -private tuple pos - position of the node.
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
### Graph
Graph this class that build the new graph . By use in nodes  we build a new structure that represent the new graph. <br/>
The class implement the interface **GraphAlgoInterface**, This interface represents a Directional Weighted Graph <br/>
The interface has a road-system or communication network in mind - and should support a large number of nodes . our implemention <br/>
based on an two dictionary that save all the edges in the graph. <br/>
***New Fields*** <br/>
- nodes -> dict()
- num_of_edge -> int
- mc -> int </br>
 Methods       | Performs | Complexity
--------------------------|-----------------------------------------|---------
Graph() | default constructor | O(1)
Graph(DirectedWeightedGraph G) | Deep copy constructor of a new graph |(1)O(n+e)
getNode(int key)               | Returns the node_data by the node_id(key). |(2) O(1)
getEdge(int src, int dest)     | Returns the data of the edge (src,dest). | (3) O(1)
addNode(NodeData n)            | Adds a new node to the graph with the given node_data. |(4) O(1)
connect(int src, int dest, double w)  | Return the weight of this edge (positive value). |(5) O(1)
nodeIter()                            |This method returns an Iterator for the nodes hashmap |
edgeIter()                    | This method returns an Iterator for all the edges in this graph. |
edgeIter(int node_id)         | This method returns an Iterator for edges getting out of the given node |
removeNode(int key)           |  Deletes the node (with the given ID) from the graph | (6) O(k), V.degree=k
removeEdge(int src, int dest) |  Deletes the edge from the graph |(7) O(1)
nodeSize() |  Returns the number of vertices (nodes) in the graph. | O(1)
edgeSize() |  Returns the number of edges (assume directional graph). | O(1)
getMC() |  Returns the Mode Count - for testing changes in the graph. | O(1)

