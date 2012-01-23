#!/usr/bin/env python

from __future__ import division, print_function

import math

import map
import gamestate
import function
import constants
import nodemap

# the main engine class
class Game:
    def __init__(self):
        self.maxplayers = 8

        # map data
        self.map = map.Map(self, "twodforttwo_remix")

        # game states
        self.current_state = gamestate.Gamestate()
        self.previous_state = self.current_state.copy()

        #self.nodemap = nodemap.Nodemap(self, self.current_state) # TO CREATE NODES, UNCOMMENT THIS

        # this accumulator is used to update the engine in fixed timesteps
        self.accumulator = 0.0

    def update(self, frametime):
        self.accumulator += frametime

        while self.accumulator >= constants.PHYSICS_TIMESTEP:
            self.accumulator -= constants.PHYSICS_TIMESTEP

            self.previous_state = self.current_state.copy()
            self.current_state.update(self, constants.PHYSICS_TIMESTEP)
