class NodeMap:
	def __init__(self,map=""):
		if map == "":
			self.generate_map()
	
	def generate_map():
		nodearray = []
		position = 0
		
		for Y in range(0,map.height):
			for X in range(0,map.width):
				if game.map.collision_mask.overlap(self,X,Y):
					nodearray[position, 'X'] = X
					nodearray[position, 'Y'] = Y
					position += 1
					
		
		