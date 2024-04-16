import random

class Graph:
    def __init__(self, adjacency_list=None, adjacency_matrix=None): # конструктор який ініціалізує граф. Приймає або список суміжності або матрицю суміжності
        self.graph_dict = {}
        if adjacency_list is not None: # якщо передано список, то граф ініціалізується з цим списком суміжності
            self.graph_dict = adjacency_list
        elif adjacency_matrix is not None: # якщо передано матрицю, викликається метод create_from_matrix для створення графа з матриці
            self.create_from_matrix(adjacency_matrix)

    def add_node(self, node): # додає нову вершину
        if node not in self.graph_dict: # якщо вона вже існує, то нічого не робить
            self.graph_dict[node] = {}

    def add_edge(self, x, y, weight=1): # додає ребро між двума вершинами з вагою(по дефолту 1)
        if x not in self.graph_dict: # перевірки чи існують вершини
            self.add_node(x)
        if y not in self.graph_dict:
            self.add_node(y)
        self.graph_dict[x][y] = weight # graph_dict[x] - словник до якого додається ключ "y" зі значенням 'weight'
        self.graph_dict[y][x] = weight # для іншої вершини також робимо, бо працюємо з ненапрямленими графами

    def remove_edge(self, x, y): # видалення ребра
        if x in self.graph_dict and y in self.graph_dict[x]:
            del self.graph_dict[x][y]
        if y in self.graph_dict and x in self.graph_dict[y]:
            del self.graph_dict[y][x]

    def remove_node(self, node): # видаляємо вершині та всі ребра які пов'язані з нею
        if node in self.graph_dict:
            for adjacent_node in list(self.graph_dict[node].keys()): # ітерація по усіх сусідніх вершинах
                self.remove_edge(node, adjacent_node)
            del self.graph_dict[node]

    def create_from_matrix(self, matrix): #створення графа з матриці
        num_nodes = len(matrix) # кількість вершин у матриці
        for i in range(num_nodes): # додавання вершин до графа
            self.add_node(i)
        for i in range(num_nodes): # додавання ребер
            for j in range(i+1, num_nodes):
                if matrix[i][j] != 0: # якщо значення в матриці не 0
                    self.add_edge(i, j, matrix[i][j]) # між вузлами додається ребро з вагою

    def get_adjacency_matrix(self):
        nodes = list(self.graph_dict.keys())
        nodes.sort() # сортуємо, щоб забезпечити порядок вершин у матриці
        size = len(nodes)
        matrix = [[0] * size for _ in range(size)] # створюється квадратна матриця з розміром кількості вершин. Поки це матриця лише з нулями
        node_index = {}
        for i, node in enumerate(nodes): # генератор словника, де ключі це вершини, а значення це їх індекси. Індекси потрібні для розміщення ваги ребер у правильні місця матриці суміжності
            node_index[node] = i
        for node, adjacents in self.graph_dict.items(): # заповнення матриці суміжності
            for adjacent, weight in adjacents.items(): # цикл проходиться через кожне суміжне ребро та його вагу.
                matrix[node_index[node]][node_index[adjacent]] = weight # вага ребер розміщується у відповідному місці матриці
        return matrix

    def display(self): # поточне представлення графа у вигляді словника
        return self.graph_dict

    def generate_random_graph(self, num_nodes, density): # випадковий зважений граф
        for i in range(num_nodes): # додавання вершин
            self.add_node(i)
        for i in range(num_nodes): # додавання ребер
            for j in range(i + 1, num_nodes):
                if random.random() < density: # density - імовірність створення ребра. Якщо рандомне число менше, то створюється ребро з рандомною вагою
                    weight = random.randint(1, 10)
                    self.add_edge(i, j, weight)



random_graph = Graph()
random_graph.generate_random_graph(10, 0.9)
print(random_graph.display())
print(random_graph.get_adjacency_matrix())
