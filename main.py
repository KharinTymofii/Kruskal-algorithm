from graph import Graph
from kruskal import Kruskal
import random
import time


# Функція для генерування випадкового графа з заданими параметрами
def generate_random_graph(num_vertices, density):
    random_graph = Graph()
    random_graph.generate_random_graph(num_vertices, density)
    return random_graph


# Задаємо список розмірів графу та щільностей
sizes = list(range(20, 201, 10))
densities = [0.1, 0.3, 0.5, 0.7, 0.9]

# Виконуємо 20 експериментів
for _ in range(20):
    size = random.choice(sizes)
    density = random.choice(densities)

    # Генеруємо випадковий граф
    random_graph = generate_random_graph(size, density)
    adjacency_matrix = random_graph.get_adjacency_matrix()

    # Запускаємо алгоритм Крускала та обчислюємо час виконання
    start_time = time.time_ns()
    kruskal_finder = Kruskal(adjacency_matrix)
    min_spanning_tree = kruskal_finder.get_min_spanning_tree()
    end_time = time.time_ns()

    # Переводимо час виконання в мілісекунди
    execution_time_ms = (end_time - start_time) / 1_000_000

    # Виводимо результати
    print(f"Граф розміру {size} з щільністю {density}:")
    print("Мінімальне остовне дерево:", min_spanning_tree)
    print("Час виконання:", execution_time_ms, "мілісекунд\n")
