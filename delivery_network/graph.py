class Graph:
    """
    Classe représentant des graphes au moyen de listes d'adjacence
    et implémentant différents algorithmes sur ceux-ci. Les graphes de
    cette classe ne sont pas orientés.

    Attributs:
    -----------
    nodes: NodeType
        La liste de noeuds du graphe. Ceux-ci peuvent être de type int, 
        float ou str mais nous privilégieront les entiers
    graph: dict
        Un dictionnaire contenant la liste d'adjacences de chaque noeuds 
        sous la forme graph[noeud] = [(voisin1, p1, d1), (voisin2, p2, d2), ...]
        où p1 est la puissance requise sur l'arrete (noeud, voisin1) et d1 
        la distance
    nb_nodes: int
        Le nombre de noeuds du graphe
    nb_edges: int
        Le nombre d'aretes du graphe 
    """

    def __init__(self, nodes=[]):
        """
        Initialise le graphe avec un ensemble de noeuds (et aucune arête).
        Parametres: 
        -----------
        nodes: liste, optionelle
            Par défaut elle sera vide.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    
    def __str__(self):
        """Affiche le graphe sous la forme d'une liste de voisins pour 
        chaque noeud (un par ligne)."""
        if not self.graph:
            output = "Le graphe est vide"            
        else:
            output = f"Le graph possède {self.nb_nodes} noeuds et {self.nb_edges} aretes.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Ajoute une arête au graphe. Les graphes n'étant pas orientés, 
        une arete est ajoutée à la liste d'adjacence des deux nœuds d'extremite.
        Parameters: 
        -----------
        node1: NodeType
            Premiere extremite de l'arete
        node2: NodeType
            Seconde extremite de l'arete
        power_min: numerique (int ou float)
            Puissance minimale sur cette arete
        dist: numerique (int ou float), optionel
            Distance entre le nœud 1 et le nœud 2 sur l'arête. La valeur 
            par defaut est 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    
    def get_path_with_power(self, src, dest, power):
        nodes_visited = {node: False for node in self.nodes}

        def dfs(node):
            if node == dest:
                return [node]
            for nei, p, _ in self.graph[node]:
                if not nodes_visited[nei] and p <= power:
                    nodes_visited[nei] = True
                    d = dfs(nei)
                    if d is not None:
                        return [node] + d
            return None
        return dfs(src)
    
    def connected_components(self):

        list_comp = []
        nodes_visited = {node: False for node in self.nodes}

        def dfs(node):
            comp = [node]
            for nei in self.graph[node]:
                nei = nei[0]
                if not nodes_visited[nei]:
                    nodes_visited[nei] = True
                    comp += dfs(nei)
            return comp
        for node in self.nodes:
            if not nodes_visited[node]:
                list_comp.append(dfs(node))
        return list_comp

    def connected_components_set(self):
        """
        Le résultat devrait être un ensemble de frozensets (un par composant), 
        Par exemple pour network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """

        return set(map(frozenset, self.connected_components()))

    def min_power(self, src, dest):
        liste = []
        for n in self.nodes:
            for i in self.graph[n]:
                liste.append(i[1])
        M = max(liste)
        a = self.get_path_with_power(src, dest, M)
        if a is None:
            return None
        while a is not None:
            M -= 1
            a = self.get_path_with_power(src, dest, M)
        p_min = M+1
        path = self.get_path_with_power(src, dest, p_min)

        return p_min, path

    
    
    
    
    
    
    
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
