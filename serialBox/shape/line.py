from abstractShape import abstractShape
from serialBox import colors
class line(abstractShape):
	def __init__(self, x, y, length, color, orientation):
		abstractShape.__init__(self, x, y, color)
		self.length = length
		self.orientation = orientation

	def draw(self, screen):
		output = ""
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += self.formatPointToString(self.x+i, self.y, self.color)
			screen.output(output)
			
		else:
			for i in range(self.length):
				output += self.formatPointToString(self.x, self.y+i, self.color)
			screen.output(output)

	def clear(self,screen):
		output = ""
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += formatPointToString(self.x+i, self.y, colors.DEFAULTBACKGROUND)
			screen.output(output)
			
		else:
			for i in range(self.length):
				output += self.formatPointToString(self.x, self.y+i, colors.DEFAULTBACKGROUND)
			screen.output(output)

	def move(self, x, y, screen):
		if x != self.x or y != self.y:
			self.clear(screen)
			self.x = x
			self.y = y
			self.draw(screen)
