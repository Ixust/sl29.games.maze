"""Module providing the Maze class"""

import networkx as nx
import random

class Maze:
    """Class representing a maze"""

    def __init__(self, width, length, height=1):
        """Initialize the maze with a 2D list of characters"""
        self.width = width
        self.length = length
        self.height = height
        # 1. Create a 3D grid graph where each node has edges to its adjacent nodes (up, down, left, right, and optionally up/down in 3D)
        self.graph = nx.grid_graph(dim=[width, length, height])

        # 2. Assign a Cell object to each node in the graph
        for node in self.graph.nodes():
            x, y, z = node # the id of the node is a tuple (x,y,z)
            self.graph.nodes[node]['data'] = Cell(node)

        # 3. Remove all edges to start with a maze full of walls
        self.graph.remove_edges_from(list(self.graph.edges()))

class Cell:
    """Class representing a cell in the maze"""

    def __init__(self, coords):
        """Initialize the cell with its coordinates"""
        self.coords = coords #(x,y,z)
