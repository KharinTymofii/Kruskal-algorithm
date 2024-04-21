class Kruskal:
    def __init__(self, graph):
        self.graph = graph

    def get_min_spanning_tree(self):
        num_nodes = len(self.graph)
        included_nodes = []  # Вершини, які вже включені в minimal spanning tree
        minimal_spanning_tree = []  # Початковий мінімальний minimal spanning tree

        # Сортуємо ребра графа за зростанням ваги
        edges = []
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if self.graph[i][j] != 0:
                    edges.append((i, j, self.graph[i][j]))

        edges.sort(key=lambda x: x[2])

        for edge in edges:
            i, j, weight = edge

            if (
                i in included_nodes and j in included_nodes
            ):  # Перевіряємо, чи вершини i та j вже включені в minimal_spanning_tree
                continue

            minimal_spanning_tree.append((i, j, weight))  # Додаємо ребро до minimal_spanning_tree
            included_nodes.append(i)  # Додаємо вершину i до включених вершин
            included_nodes.append(j)  # Додаємо вершину j до включених вершин

        return minimal_spanning_tree  # Повертаємо мінімальний minimal spanning tree
