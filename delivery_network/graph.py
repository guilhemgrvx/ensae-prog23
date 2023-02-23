class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
       
       self.nb_edges +=1
       self.graph[node1].append((node2, power_min, dist))
       self.graph[node2].append((node1, power_min, dist))
       raise NotImplementedError
    

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError
    

    def connected_components(self):
        raise NotImplementedError


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """

    with open(filename) as file:
        ligne1= file.readline().split()
        n=int(ligne1[0])
        m=int(ligne1[1])
        nodes=[i for i in range(1,n+1)]
        G=graph(nodes)
        for i in range(m):
            lignei= file.readline().split()
            node1=int(lignei[0])
            node2=int(lignei[1])
            power_min=int(lignei[2])
            if len(lignei) > 3:
                dist = int(lignei[3])
                G.add_edge(node1, node2, power_min, dist)
            else :
                G.add_edge(node1, node2, power_min)
    return G

    raise NotImplementedError