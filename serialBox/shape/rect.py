from shape import shape
class rect(shape):

	def __init__(self, x, y, width, height, color):
		AbstractShape.__init__(self, x, y, color)
		self.width = width
		self.height = height

	def draw(self,screen):
		output = ""
		for i in range(self.height):
			for j in range(self.width):
				output += formatPointToString(self.x + i, self.y + j)
		screen.output(output)


	def clear(self):
		pass

	def move(self):
		pass