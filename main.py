from graph import Graph
from kruskal import Kruskal
import time
import csv


# Функція для генерування графа з заданими параметрами
def generate_graph(num_vertices, density):
    random_graph = Graph()
    random_graph.generate_random_graph(num_vertices, density)
    return random_graph.get_adjacency_matrix()


# Функція для обчислення метрик
def calculate_metrics(min_spanning_tree):
    num_edges = len(min_spanning_tree)
    total_weight = sum(weight for _, _, weight in min_spanning_tree)
    min_weight = min(min_spanning_tree, key=lambda x: x[2])[2]
    max_weight = max(min_spanning_tree, key=lambda x: x[2])[2]
    return num_edges, total_weight / num_edges, min_weight, max_weight


# Відкриваємо файл для запису результатів у форматі CSV
with open("results.csv", "w", newline="") as csvfile:
    fieldnames = [
        "Density",
        "Vertices",
        "Time (ms)",
        "Edges",
        "Mean Weight",
        "Min Weight",
        "Max Weight",
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
            num_edges, mean_weight, min_weight, max_weight = calculate_metrics(
                min_spanning_tree
            )

            # Записуємо результати в файл у форматі CSV
            writer.writerow(
                {
                    "Density": density,
                    "Vertices": num_vertices,
                    "Time (ms)": execution_time_ms,
                    "Edges": num_edges,
                    "Mean Weight": mean_weight,
                    "Min Weight": min_weight,
                    "Max Weight": max_weight,
                }
            )

            # Виводимо результати у консоль
            print(f"Density: {density}, Vertices: {num_vertices}")
            print("Time (ms):", execution_time_ms)
            print("Edges:", num_edges)
            print("Mean Weight:", mean_weight)
            print("Min Weight:", min_weight)
            print("Max Weight:", max_weight)
            print()

print("Results saved to results.csv")