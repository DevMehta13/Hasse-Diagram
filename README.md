# Hasse Diagram Generator for Divisibility Posets

## Overview
This project provides a Python-based tool to generate and visualize Hasse diagrams for partially ordered sets (posets) where the ordering relation is defined by divisibility (a divides b). The diagram is constructed using a directed acyclic graph (DAG), where each node represents an element in the poset, and each directed edge represents the divisibility relation.

## How It Works
### Logic
1.	Divisibility Relation:
- The poset is defined by a set of elements where the relation a divides b is used to establish order between any two elements a and b.
- A Hasse diagram is constructed by adding directed edges from a to b if a divides b and no intermediate element exists such that a divides that element and that element divides b.

3.	Graph Representation:
- The elements of the poset are represented as nodes in a directed acyclic graph (DAG).
- Edges are added between nodes according to the divisibility relation.
- Transitive edges are removed to ensure the minimal representation, characteristic of Hasse diagrams.

5.	Visualization:
- The graph is plotted using matplotlib, with nodes positioned according to their levels in the poset hierarchy.
- Arrows are used to indicate the direction of the divisibility relation, with larger elements at higher levels and smaller elements at lower levels.

### Features
- User Input: The program accepts user input for the elements of the poset.
- Graph Generation: Automatically generates the corresponding Hasse diagram based on the divisibility relation.
- Visualization: Displays the diagram with arrows indicating the direction of the divisibility relation.
  
### Functions

1.	 is_divisible(a, b)
- Description: Checks if a divides b without a remainder.
- Parameters:
   - a (int): The potential divisor.
   - b (int): The number to be divided.
- Returns: True if a divides b, otherwise False.

3.	 generate_hasse_diagram(elements)
- Description: Generates the directed acyclic graph (DAG) representing the Hasse diagram for the given elements.
- Parameters:
      - elements (list of int): The list of elements in the poset.
- Returns: A NetworkX DiGraph object representing the Hasse diagram.

5.	 get_node_levels(G)
- Description: Calculates the level (or height) of each node in the Hasse diagram, where the level corresponds to the node's position in the hierarchy.
- Parameters:
     - G (NetworkX DiGraph): The graph representing the Hasse diagram. 
- Returns: A dictionary mapping each node to its level.

7.	plot_hasse_diagram(G)
- Description: Visualizes the Hasse diagram using matplotlib, with nodes positioned according to their level and arrows indicating divisibility relations.
- Parameters:
    - G (NetworkX DiGraph): The graph representing the Hasse diagram.

9.	main()
- Description: The main function that prompts the user for input, generates the Hasse diagram, and displays it.
  
## Usage
1.	Run the Program:
- Execute the script in a Python environment. It will prompt you to enter the elements of the poset.

2.	Input:
- Enter the elements of the poset as a space-separated list of integers (e.g., 1 2 3 4 6 12).

3.	Output:
- The program will generate and display the Hasse diagram for the entered poset, with arrows showing the direction of divisibility.

## Requirements
- Python 3.x
- NetworkX
- Matplotlib

## Installation
- Install the required packages using pip:
  ```bash
pip install networkx matplotlib

 
## Example
Enter the elements of the poset separated by spaces (e.g., 1 2 3 4 6 12): 1 2 3 4 6 12
This input will generate a Hasse diagram with 1 at the top, 12 at the bottom, and edges showing the divisibility relationships among the elements.
 
![image](https://github.com/user-attachments/assets/9ee1ef82-285d-4354-af80-1b3c8e87d8ed)
