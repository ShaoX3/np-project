import networkx as nx
import random
import matplotlib.pyplot as plt
G = nx.Graph()
for i in range(50):
    G.add_node("child " + str(i))
for x in range(50):
    for y in range(x, 50):
        r = random.uniform(0,1)
        if r >= 0.5:
            G.add_edge("child " + str(x), "child " + str(y))

nx.draw(G, with_labels = True)
nx.write_gml(G, "Small.gml")