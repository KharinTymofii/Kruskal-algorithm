from graph import Graph
from kruskal import Kruskal
import time
import csv


# Функція для генерування графа з заданими параметрами
def generate_graph(num_vertices, density):
    random_graph = Graph()
    random_graph.generate_random_graph(num_vertices, density)
    return random_graph


# Відкриваємо файл для запису результатів у форматі CSV
with open("results.csv", "w", newline="") as csvfile:
    fieldnames = [
        "Density",
        "Vertices",
        "Avg Time from matrix (ms)",
        "Avg Time from list (ms)",
        "Avg Edges",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Генеруємо графи та рахуємо метрики
    for density in [round(0.5 + 0.1 * i, 1) for i in range(5)]:
        for num_vertices in range(20, 201, 20):
            total_time_matrix_ms = 0
            total_time_adjacency_list_ms = 0
            total_edges = 0

            # Виконуємо алгоритм п'ять разів
            for _ in range(5):
                graph = generate_graph(num_vertices, density)

                start_time_adjacency_list = time.time_ns()
                min_spanning_tree_adjacency_list = Kruskal.get_mts_from_adjacency_list(
                    graph.get_adjacency_list()
                )
                end_time_adjacency_list = time.time_ns()
                start_time_matrix = time.time_ns()
                min_spanning_tree_matrix = Kruskal.get_mst_from_adjacency_matrix(
                    graph.get_adjacency_matrix()
                )
                end_time_matrix = time.time_ns()

                execution_matrix_time_ms = (
                    end_time_matrix - start_time_matrix
                ) / 1_000_000

                total_time_matrix_ms += execution_matrix_time_ms


                execution_adjacency_list_time_ms = (
                    end_time_adjacency_list - start_time_adjacency_list
                ) / 1_000_000
                total_time_adjacency_list_ms += execution_adjacency_list_time_ms

                num_edges = len(min_spanning_tree_matrix)
                total_edges += num_edges

            # Беремо середнє значення часу виконання та кількості ребер
            avg_time_matrix_ms = total_time_matrix_ms / 5
            avg_time_adjacency_list_ms = total_time_adjacency_list_ms / 5
            avg_edges = total_edges / 5

            # Записуємо результати в файл у форматі CSV
            writer.writerow(
                {
                    "Density": density,
                    "Vertices": num_vertices,
                    "Avg Time from matrix (ms)": avg_time_matrix_ms,
                    "Avg Time from list (ms)": avg_time_adjacency_list_ms,
                    "Avg Edges": avg_edges,
                }
            )

            # Виводимо результати у консоль
            print(f"Density: {density}, Vertices: {num_vertices}")
            print("Avg Time from matrix (ms):", avg_time_matrix_ms)
            print("Avg Time from list (ms):", avg_time_adjacency_list_ms)
            print("Avg Edges:", avg_edges)
            print()

print("Results saved to results.csv")
