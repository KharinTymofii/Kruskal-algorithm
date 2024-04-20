from graph import Graph

random_graph = Graph()
random_graph.generate_random_graph(10, 0.9)
print(random_graph.display())
print(random_graph.get_adjacency_matrix(random_graph))
