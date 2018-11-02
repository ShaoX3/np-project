import networkx as nx
G = nx.Graph()
G.add_nodes_from(["Jared", "Peter", "Trisha"])
G.add_edges_from([("Jared", "Peter"), ("Trista", "Peter"), ("Jared", "Trisha")])
nx.write_gml(G, "TestGraph.gml")
