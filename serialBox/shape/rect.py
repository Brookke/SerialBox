from shape import shape
class rect(shape):

	def __init__(self, x, y, width, height, color):
		AbstractShape.__init__(self, x, y, color)
		self.width = width
		self.height = height

	def draw(self):
		pass

	def clear(self):
		pass

	def move(self):
		pass