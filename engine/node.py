from __future__ import division

import functions, mask
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

    def add_connection(self, othernode, distance, command):
        self.connection_nodes.append(othernode)
        self.connection_distances.append(distance)
        self.connection_commands.append(command)
