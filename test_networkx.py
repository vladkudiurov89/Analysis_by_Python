import networkx as nx
import itertools
import numpy.random as rnd

import matplotlib.pyplot as plt
from numpy import double

graph = nx.Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')


def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


add_edge('A', 'B', graph=graph)
add_edge('B', 'C', graph=graph)
add_edge('B', 'D', graph=graph)
add_edge('D', 'E', graph=graph)

nx.draw_circular(graph, node_color='red',
                 node_size=3000, with_labels=True)

plt.show()

cities = {'A': (0, 20),
          'B': (15, 24),
          'C': (16, 41),
          'D': (10, 40),
          'E': (24, 31)}

graph_1 = nx.Graph()
graph.add_nodes_from(cities)

kilometres = {('A', 'B', 15),
              ('B', 'C', 16),
              ('B', 'D', 25),
              ('C', 'D', 14),
              ('D', 'A', 18),
              ('D', 'E', 42)}

graph_1.add_weighted_edges_from(kilometres)
nx.draw_circular(graph_1, node_color='blue',
                 node_size=1000, with_labels=True)
plt.show()


def complete_graph(num: int) -> nx.Graph:
    graph_2 = nx.Graph()
    n_range = range(num)
    all_pairs = itertools.permutations(n_range, 2)
    graph_2.add_nodes_from(n_range)
    graph_2.add_edges_from(all_pairs)
    return graph_2


graph_3 = complete_graph(6)
nx.draw_circular(graph_3, node_color='y',
                 node_size=750, with_labels=True)
plt.show()


def random_graph(n: int, p: double) -> nx.Graph:
    graph_4 = nx.Graph()
    n_range = range(n)
    graph_4.add_nodes_from(n_range)
    for pair in itertools.permutations(n_range, 2):
        if rnd.random() < p:
            graph_4.add_edge(*pair)

    return graph_4


graph_5 = random_graph(7, 0.5)
nx.draw_circular(graph_5, node_color='green',
                 node_size=1000, with_labels=True)
plt.show()


def is_complete(graph_6: nx.Graph) -> bool:
    edges = len(graph_6.edges())
    nodes = len(graph_6.nodes())
    return edges == nodes * (nodes - 1) / 2


print(is_complete(complete_graph(5)))
print(is_complete(random_graph(10, 0.7)))