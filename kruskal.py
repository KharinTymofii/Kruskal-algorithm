class Kruskal:
    def get_mst_from_edges(edges):
        included_nodes = []  # Вершини, які вже включені в minimal spanning tree
        minimal_spanning_tree = []  # Початковий мінімальний minimal spanning tree

        for edge in edges:
            i, j, weight = edge

            if (
                i in included_nodes and j in included_nodes
            ):  # Перевіряємо, чи вершини i та j вже включені в minimal_spanning_tree
                continue

            minimal_spanning_tree.append(
                (i, j, weight)
            )  # Додаємо ребро до minimal_spanning_tree
            included_nodes.append(i)  # Додаємо вершину i до включених вершин
            included_nodes.append(j)  # Додаємо вершину j до включених вершин

        return minimal_spanning_tree  # Повертаємо мінімальний minimal spanning tree

    def get_mst_from_adjacency_matrix(adjacency_matrix):
        num_nodes = len(adjacency_matrix)

        # Створюємо список ребер графа
        
        edges = []
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if adjacency_matrix[i][j] != 0:
                    edges.append((i, j, adjacency_matrix[i][j]))

        # Сортуємо ребра графа за зростанням ваги
        edges.sort(key=lambda x: x[2])

        return Kruskal.get_mst_from_edges(edges)

    def get_mts_from_adjacency_list(adjacency_list):
        # Створюємо список ребер графа
        edges = []
        for node, adjacents in adjacency_list.items():
            for adjacent, weight in adjacents.items():
                edges.append((node, adjacent, weight))

        # Сортуємо ребра графа за зростанням ваги
        edges.sort(key=lambda x: x[2])

        return Kruskal.get_mst_from_edges(edges)
