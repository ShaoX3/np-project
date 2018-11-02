import networkx as nx
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_edges_from([("A", "D"), ("D", "F"), ("F", "C"), ("C", "E"), ("E", "B"), ("B", "F")])
nx.write_gml(G, "graph.gml")
