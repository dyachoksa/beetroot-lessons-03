class Graph:
    def __init__(self, graph_dict=None) -> None:
        if graph_dict is not None and type(graph_dict) is not dict:
            raise ValueError("the initial graph data should be dictionary or None")

        self.graph_dict = graph_dict if graph_dict is not None else {}
    
    def get_edges(self, node):
        return self.graph_dict[node]

    def get_all_nodes(self):
        return list(self.graph_dict.keys())

    def get_all_edges(self):
        edges = []

        for node in self.graph_dict:
            for right_node in self.graph_dict[node]:
                if tuple({node, right_node}) not in edges:
                    edges.append((node, right_node))

        return edges

    def add_node(self, node):
        if node not in self.graph_dict:
            self.graph_dict[node] = []

        return self
    
    def add_edge(self, node1, node2):
        for x, y in [(node1, node2), (node2, node1)]:
            if x in self.graph_dict:
                self.graph_dict[x].append(y)
            else:
                self.graph_dict[x] = [y]
    
    def find_path(self, start_node, end_node, path=None):
        path = path if path is not None else []

        path = path + [start_node]

        if start_node == end_node:
            return path
        
        if start_node not in self.graph_dict:
            return None

        for node in self.graph_dict[start_node]:
            if node not in path:
                inner_path = self.find_path(node, end_node, path)
                if inner_path:
                    return inner_path
        
        return None
    
    def find_all_paths(self, start_node, end_node, path=[]):
        path = path + [start_node]

        if start_node == end_node:
            return [path]
        
        if start_node not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start_node]:
            if node not in path:
                inner_paths = self.find_all_paths(node, end_node, path)
                
                for p in inner_paths:
                    paths.append(p)
        
        return paths
    
    def get_shortest_path(self, start_node, end_node):
        paths = self.find_all_paths(start_node, end_node)
        return sorted(paths, key=len)[0]

def main():
    initial_graph = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": [],
    }

    print("\n Graph 1")
    graph = Graph(initial_graph)

    print("Edges of 'd'", graph.get_edges("d"))
    print("All nodes:", graph.get_all_nodes())
    print("All edges:", graph.get_all_edges())

    print("Add node 'g' with edges 'gd' and 'ge'")
    graph.add_node("g")
    graph.add_edge("g", "d")
    graph.add_edge("g", "e")

    print("All nodes:", graph.get_all_nodes())
    print("All edges:", graph.get_all_edges())

    print("Path from 'a' to 'g':", graph.find_path("a", "g"))
    print("All paths from 'a' to 'g':", graph.find_all_paths("a", "g"))
    print("Shortest paths from 'a' to 'g':", graph.get_shortest_path("a", "g"))

    g = {
        "a" : {"d", "f"},
        "b" : {"c"},
        "c" : {"b", "c", "d", "e"},
        "d" : {"a", "c", "f"},
        "e" : {"c"},
        "f" : {"a", "d"}
    }

    print("\n Graph 2")

    graph1 = Graph(g)
    print("All nodes:", graph1.get_all_nodes())
    print("All edges:", graph1.get_all_edges())
    print("Path from 'a' to 'f':", graph1.find_path("a", "f"))
    print("All paths from 'a' to 'b':", graph1.find_all_paths("a", "b"))
    print("All paths from 'a' to 'f':", graph1.find_all_paths("a", "f"))
    print("Shortest paths from 'a' to 'f':", graph1.get_shortest_path("a", "f"))


if __name__ == "__main__":
    main()
