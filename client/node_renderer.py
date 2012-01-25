from __future__ import division

import function, pygrafix

class NodeRenderer(object):
    def __init__(self):
        self.sprite = function.load_image("red_circle")
        self.radius = 5

    def render(self, renderer, game, state, node):

        sprite = pygrafix.sprite.Sprite(self.sprite)

        sprite.position = renderer.get_screen_coords(node.x-self.radius, node.y-self.radius)
        sprite.alpha = 0.5

        renderer.world_sprites.add_sprite(sprite)
