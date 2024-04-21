from graph import Graph
from kruskal import Kruskal
import time
import csv


# Функція для генерування графа з заданими параметрами
def generate_graph(num_vertices, density):
    random_graph = Graph()
    random_graph.generate_random_graph(num_vertices, density)
    return random_graph.get_adjacency_matrix()


# Відкриваємо файл для запису результатів у форматі CSV
with open("results.csv", "w", newline="") as csvfile:
    fieldnames = [
        "Density",
        "Vertices",
        "Avg Time (ms)",
        "Avg Edges",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Генеруємо графи та рахуємо метрики
    for density in [round(0.5 + 0.1 * i, 1) for i in range(6)]:
        for num_vertices in range(20, 201, 20):
            total_time_ms = 0
            total_edges = 0

            # Виконуємо алгоритм п'ять разів
            for _ in range(5):
                adjacency_matrix = generate_graph(num_vertices, density)

                start_time = time.time_ns()
                kruskal_finder = Kruskal(adjacency_matrix)
                min_spanning_tree = kruskal_finder.get_min_spanning_tree()
                end_time = time.time_ns()

                execution_time_ms = (end_time - start_time) / 1_000_000
                num_edges = len(min_spanning_tree)

                total_time_ms += execution_time_ms
                total_edges += num_edges

            # Беремо середнє значення часу виконання та кількості ребер
            avg_time_ms = total_time_ms / 5
            avg_edges = total_edges / 5

            # Записуємо результати в файл у форматі CSV
            writer.writerow(
                {
                    "Density": density,
                    "Vertices": num_vertices,
                    "Avg Time (ms)": avg_time_ms,
                    "Avg Edges": avg_edges,
                }
            )

            # Виводимо результати у консоль
            print(f"Density: {density}, Vertices: {num_vertices}")
            print("Avg Time (ms):", avg_time_ms)
            print("Avg Edges:", avg_edges)
            print()

print("Results saved to results.csv")
