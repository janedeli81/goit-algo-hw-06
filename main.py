import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинок) та ребер (маршрутів) до графа
stops = ["Зупинка 1", "Зупинка 2", "Зупинка 3", "Зупинка 4", "Зупинка 5",
         "Зупинка 6", "Зупинка 7", "Зупинка 8", "Зупинка 9", "Зупинка 10"]
routes = [("Зупинка 1", "Зупинка 2"), ("Зупинка 2", "Зупинка 3"), ("Зупинка 3", "Зупинка 4"),
          ("Зупинка 4", "Зупинка 5"), ("Зупинка 5", "Зупинка 6"), ("Зупинка 6", "Зупинка 7"),
          ("Зупинка 7", "Зупинка 8"), ("Зупинка 8", "Зупинка 9"), ("Зупинка 9", "Зупинка 10"),
          ("Зупинка 10", "Зупинка 1"), ("Зупинка 1", "Зупинка 5"), ("Зупинка 2", "Зупинка 6"),
          ("Зупинка 3", "Зупинка 7"), ("Зупинка 4", "Зупинка 8"), ("Зупинка 5", "Зупинка 9")]
G.add_nodes_from(stops)
G.add_edges_from(routes)

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', font_size=10)
plt.title("Модель транспортної мережі міста")
plt.show()

# Пошук шляхів за допомогою DFS і BFS
start_stop = "Зупинка 1"
end_stop = "Зупинка 10"

# DFS
dfs_paths = list(nx.all_simple_paths(G, start_stop, end_stop))
dfs_path = dfs_paths[0] if dfs_paths else None

# BFS
bfs_path = nx.shortest_path(G, start_stop, end_stop)

print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)

# Створення графа з вагами для ребер
G_weighted = nx.Graph()
G_weighted.add_nodes_from(stops)
for u, v in routes:
    weight = random.randint(1, 10)  # Вага ребра
    G_weighted.add_edge(u, v, weight=weight)

# Використання алгоритму Дейкстри
dijkstra_paths = dict(nx.all_pairs_dijkstra_path(G_weighted))
dijkstra_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G_weighted))

# Відображення шляхів та довжин для "Зупинка 1"
example_start = "Зупинка 1"
example_paths = dijkstra_paths[example_start]
example_lengths = dijkstra_path_lengths[example_start]

print("\nНайкоротші шляхи з 'Зупинка 1':", example_paths)
print("Довжини шляхів з 'Зупинка 1':", example_lengths)
