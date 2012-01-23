from __future__ import division

import function

class NodeRenderer(object):
    def __init__(self):
        self.sprite = function.load_image("circle_red.png")

    def render(self, renderer, game, state, node):

        sprite = pygrafix.sprite.Sprite(self.sprite)

        sprite.position = renderer.get_screen_coords(node.x, node.y)
        sprite.alpha = 0.5

        renderer.world_sprites.add_sprite(sprite)
