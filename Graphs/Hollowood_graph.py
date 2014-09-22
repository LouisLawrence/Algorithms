import networkx as nx

ex1 = nx.Graph()
#left side
ex1.add_edge("Kevin Bacon", "Michael Fassbender", data={"film": "x-men: first class"})
ex1.add_edge("Micheal Fassbender", "Noomi Rapace")
ex1.add_edge("Lasco Atkins", "Noomi Rapace")
ex1.add_edge("Kevin Bacon", "Lasco Atkins")
ex1.add_edge("Kevin Bacon", "David Crown")
ex1.add_edge("Idris Elba", "David Crown")
ex1.add_edge("Idris Elba", "Michael Fassbender")
#right side

ex1.add_edge("Kevin Bacon", "Richard Frice")
ex1.add_edge("Rasario Dawson", "Richard Frice")
ex1.add_edge("Rasario Dawson", "James McAvoy")
ex1.add_edge("Kevin Bacon", "James McAvoy")
ex1.add_edge("James McAvoy", "Vicent Cassel")
ex1.add_edge("Kevin Bacon", "Scott Cann")
ex1.add_edge("Vicent Cassel", "Scott Cann")

print(nx.neighbors(ex1, "Kevin Bacon"))
print(nx.degree(ex1, "Kevin Bacon"))
