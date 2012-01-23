from __future__ import division

import function, mask
from entity import Entity

class Node(Entity):
    def __init__(self, game, state, (x, y)):
        Entity.__init__(self, game, state)

        self.x = x
        self.y = y

        self.connection_nodes = [] # All the nodes to which this one is connected
        self.connection_distances = [] # The distances to those nodes
        self.connection_commands = [] # The commands to get to that connection

        self.history = [] # When searching a path, this is the path from the source node to this one
        self.pathlength

    def add_connection(self, othernode, distance, command):
        self.connection_nodes.append(othernode)
        self.connection_distances.append(distance)
        self.connection_commands.append(command)

    def search_path(self, target):
        # Recursive function that goes through all node connections until it finds a target node
        self.history.append(self)

        if self == target:
            return self.history

        for node in self.connection_nodes:
            # Skip any nodes who have already been considered
            if node in self.history:
                continue

            # Compare the current path length of that other node with the current one
            possible_pathlength = self.pathlength+self.connection_distances[self.connection_nodes.index(node)]
            if node.pathlength > possible_pathlength:
                node.history = self.history[:]
                node.pathlength = possible_pathlength
                path = node.searchpath(target)# Let it calculate it's neighbours too, until it returns either None or a path
                if path != None:
                    return path

        return None # Nothing here
