#!/usr/bin/env python

from __future__ import division, print_function

import math

import map
import character
import gamestate
import function
import constants
import player

# the main engine class
class Game:
    def __init__(self):
        # map data
        self.map = map.Map(self, "twodforttwo_remix")

        # game states
        self.current_state = gamestate.Gamestate()

        self.player = player.Player(self, self.current_state)
        
        self.previous_state = self.current_state.copy()

        # this accumulator is used to update the engine in fixed timesteps
        self.accumulator = 0.0

    def update(self, frametime):
        self.accumulator += frametime

        while self.accumulator >= constants.PHYSICS_TIMESTEP:
            self.accumulator -= constants.PHYSICS_TIMESTEP

            self.previous_state = self.current_state.copy()
            self.current_state.update(self, constants.PHYSICS_TIMESTEP)