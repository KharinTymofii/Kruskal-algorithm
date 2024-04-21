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
        "Time (ms)",
        "Edges",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # Генеруємо графи та рахуємо метрики
    for density in [round(0.5 + 0.1 * i, 1) for i in range(6)]:
        for num_vertices in range(20, 201, 20):
            adjacency_matrix = generate_graph(num_vertices, density)

            start_time = time.time_ns()
            kruskal_finder = Kruskal(adjacency_matrix)
            min_spanning_tree = kruskal_finder.get_min_spanning_tree()
            end_time = time.time_ns()

            execution_time_ms = (end_time - start_time) / 1_000_000
            num_edges = len(min_spanning_tree)

            # Записуємо результати в файл у форматі CSV
            writer.writerow(
                {
                    "Density": density,
                    "Vertices": num_vertices,
                    "Time (ms)": execution_time_ms,
                    "Edges": num_edges,
                }
            )

            # Виводимо результати у консоль
            print(f"Density: {density}, Vertices: {num_vertices}")
            print("Time (ms):", execution_time_ms)
            print("Edges:", num_edges)
            print()

print("Results saved to results.csv")
