import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def is_divisible(a, b):
    return b % a == 0

def generate_hasse_diagram(elements):
    G = nx.DiGraph()

    elements = sorted(elements)
    G.add_nodes_from(elements)

    for a, b in combinations(elements, 2):
        if is_divisible(a, b):
            G.add_edge(a, b)

    for node in elements:
        descendants = nx.descendants(G, node)
        for d in descendants:
            for intermediate in nx.descendants(G, d):
                if G.has_edge(node, intermediate):
                    G.remove_edge(node, intermediate)
    
    return G

def get_node_levels(G):
    levels = {}
    for node in nx.topological_sort(G):
        pred_levels = [levels[p] for p in G.predecessors(node)]
        levels[node] = 0 if not pred_levels else max(pred_levels) + 1
    return levels

def plot_hasse_diagram(G):
    levels = get_node_levels(G)
    sorted_nodes = sorted(G.nodes(), key=lambda x: (levels[x], x))

    pos = {}
    level_positions = {}
    for node in sorted_nodes:
        level = levels[node]
        if level not in level_positions:
            level_positions[level] = 0
        pos[node] = (level_positions[level], level)  
        level_positions[level] += 1

    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=15, 
            font_weight="bold", arrows=True, arrowstyle='->', arrowsize=20)
    plt.show()

def main():
    user_input = input("Enter the elements of the poset separated by spaces (e.g., 1 2 3 4 6 12): ")
    
    elements = list(map(int, user_input.split()))
    
    G = generate_hasse_diagram(elements)
    plot_hasse_diagram(G)

if __name__ == "__main__":
    main()
