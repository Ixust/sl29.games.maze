"""Module providing the Maze class"""

import random
import matplotlib.pyplot as plt
import networkx as nx

class Maze:
    """Class representing a maze"""

    def __init__(self, width:int, length:int, height=1):
        """Initialize the maze with a 2D list of characters"""
        self.width = width
        self.length = length
        self.height = height

        # 1. Create a 3D grid graph where each node has edges to its adjacent nodes
        # -> forward, backward, left and right
        self.graph = nx.grid_graph(dim=[width, length, height])

        # 2. Assign a Cell object to each node in the graph
        for node in self.graph.nodes():
        # x, y, z = node # the id of the node is a tuple (x,y,z)
            self.graph.nodes[node]['data'] = Cell(node)

        # 3. Remove all edges to start with a maze full of walls
        self.graph.remove_edges_from(list(self.graph.edges()))

    def passage(self, c1:'Cell', c2:'Cell'):
        """Makes a passage from c1 to c2"""
        x1, y1 = c1['data'].coords[2], c1['data'].coords[1]
        x2, y2 = c2['data'].coords[2], c2['data'].coords[1]
        if x2-x1 == 1 or x1-x2 == 1 or y2-y1 == 1 or y1-y2 == 1:
            self.graph.add_edge(c1['data'],c2['data'])

    def create(self, maze:'Maze')->'Maze':
        """Creates a operational maze from one full of walls"""
        if maze.width == 1:
            for k in range(maze.length-1):
                self.passage(maze.graph.nodes[(0,k,0)],maze.graph.nodes[(0,k+1,0)])
        elif maze.length == 1:
            for k in range(maze.width-1):
                self.passage(maze.graph.nodes[(0,0,k)],maze.graph.nodes[(0,0,k+1)])
        elif maze.width >= maze.length:
            self.create(Maze(maze.width, maze.length//2))
            self.create(Maze(maze.width, maze.length-maze.length//2))
            self.passage(maze.graph.nodes[(0,0,maze.length//2)], maze.graph.nodes[(0,0,maze.length//2+1)])
        else:
            self.create(Maze(maze.width//2, maze.length))
            self.create(Maze(maze.width-maze.width//2, maze.length))
            self.passage(maze.graph.nodes[(0,maze.width//2,0)], maze.graph.nodes[(0,maze.width//2+1,0)])
        return maze

class Cell:
    """Class representing a cell in the maze"""

    def __init__(self, coords:tuple):
        """Initialize the cell with its coordinates"""
        self.coords = coords #(x,y,z)

def plot_maze_3d(maze:Maze):
    """Visual representation of the maze in 3d"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # On récupère les positions des nœuds directement depuis les tuples (x, y, z)
    # pos = {node: node for node in maze.graph.nodes()}

    # On dessine les arêtes (les passages ouverts)
    for edge in maze.graph.edges():
        x = [edge[0].coords[0], edge[1].coords[0]]
        y = [edge[0].coords[1], edge[1].coords[1]]
        z = [edge[0].coords[2], edge[1].coords[2]]
        ax.plot(x, y, z, color='blue', alpha=0.6)

    # On dessine les nœuds
    nodes = list(maze.graph.nodes())[0:maze.length*maze.width]
    ax.scatter([n[0] for n in nodes], [n[1] for n in nodes], [n[2] for n in nodes], c='red', s=20)

    plt.show()

maze1= Maze(5,5)
#node = maze1.graph.nodes[(0,2,2)]
#print(node)
maze1.create(maze1)
plot_maze_3d(maze1)
