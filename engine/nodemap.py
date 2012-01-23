from __future__ import division

import node

class Nodemap(object):
    def __init__(self, game, state, nodemap=""):
        if nodemap == "":
            self.generate_nodes(game, state)
        # TODO: Implement this function. Use struct.
        #else:
        #	self.load_nodes()

    def generate_nodes(self, game, state):
        self.nodelist = []
        mask = game.map.collision_mask
        mask_width = mask.get_size()[0]
        mask_height = mask.get_size()[1]

        onPlane = False

        # FIXME: THIS CRASHES MY COMPUTER. HELP
        # To execute, uncomment stuff in engine.game init

        for y in range(mask_height):
            for x in range(mask_width):

                if onPlane:
                    if x == 0:# We changed map row
                        self.nodelist.append(node.Node(game, state, (map_width, y-1)))
                        onPlane = False

                if (not mask.get_at((x, y))) and mask.get_at((x, y+1)):# If this is a floor pixel
                   if not onPlane: # If it's the first pixel of a certain plane
                        self.nodelist.append(node.Node(game, state, (x, y)))
                        onPlane = True

                else:# We're off the ground, but we were a pixel ago. Also, we're not at the beginning of the screen.
                    self.nodelist.append(node.Node(game, state, (x-1, y)))
                    onPlane = False
