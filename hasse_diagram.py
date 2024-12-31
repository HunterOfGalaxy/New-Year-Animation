import networkx as nx
import matplotlib.pyplot as plt

# Define relations
edges = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 8), (6, 12)]

# Create directed graph
G = nx.DiGraph(edges)

# Draw Hasse diagram
nx.draw(G, with_labels=True, node_size=1000, node_color='lightblue')
plt.show()
