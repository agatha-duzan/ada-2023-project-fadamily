# Helper function for plotting the degree distribution of a Graph
import networkx as nx
from matplotlib import pyplot as plt


def plot_degree_distribution(G, fig_size=(10, 6)):
    degrees = {}
    for node in G.nodes():
        degree = G.degree(node)
        if degree not in degrees:
            degrees[degree] = 0
        degrees[degree] += 1
    sorted_degree = sorted(degrees.items())
    deg = [k for (k, v) in sorted_degree]
    cnt = [v for (k, v) in sorted_degree]
    fig, ax = plt.subplots(figsize=fig_size)
    plt.bar(deg, cnt, width=0.80, color='b')
    plt.title("Degree Distribution")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.05 for d in deg])
    ax.set_xticklabels(deg)


def describe_graph(G):
    print(G)
    if nx.is_connected(G):
        print("Avg. Shortest Path Length: %.4f" % nx.average_shortest_path_length(G))
        print("Diameter: %.4f" % nx.diameter(G))  # Longest shortest path
    else:
        print("Graph is not connected")
        print("Diameter and Avg shortest path length are not defined!")
    print("Sparsity: %.4f" % nx.density(G))  # #edges/#edges-complete-graph
    # #closed-triplets(3*#triangles)/#all-triplets
    print("Global clustering coefficient aka Transitivity: %.4f" % nx.transitivity(G))
