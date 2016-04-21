from abstractShape import abstractShape
from serialBox import colors
class rect(abstractShape):

	def __init__(self, x, y, width, height, color):
		abstractShape.__init__(self, x, y, color)
		self.width = width
		self.height = height

	def draw(self,screen):
		output = ""
		for i in range(self.height):
			for j in range(self.width):
				output += self.formatPointToString(self.x+i, self.y+j, self.color)
		screen.output(output)


	def clear(self, screen):
		output = ""
		for i in range(self.height):
			for j in range(self.width):
				output += self.formatPointToString(self.x+i, self.y+j, colors.DEFAULTBACKGROUND)
		screen.output(output)

	def move(self):
		pass