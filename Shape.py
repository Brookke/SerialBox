from abc import ABCMeta, abstractmethod

class AbstractShape:
	__metaclass__ = ABCMeta

	def __init__(self,x,y,color):
		self.x = x
		self.y = y
		self.color = color

	@abstractmethod
	def draw(self):
		pass

	@abstractmethod
	def move(self, x, y):
		pass

	@abstractmethod
	def clear(self):
		pass

class Line(AbstractShape):
	def __init__(self, x, y, length, color, orientation):
		AbstractShape.__init__(self, x, y, color)
		self.length = length
		self.orientation = orientation

	def draw(self, screen):
		output = ""
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += formatPointToString(self.x, self.y+i, self.color)
			screen.output(output)
			
		else:
			for i in range(self.length):
				output += formatPointToString(self.x+i, self.y, self.color)
			screen.output(output)

	def move(self, x, y):
		pass

	def clear(self):
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += formatPointToString(self.x, self.y+i, DEFAULTBACKGROUND)
			surface.output(output)
			
		else:
			for i in range(self.length):
				output += formatPointToString(self.x+i, self.y, DEFAULTBACKGROUND)
			surface.output(output)

class Rect(AbstractShape):
	"""docstring for Rect"""
	def __init__(self, x, y, width, height, color):
		AbstractShape.__init__(self, x, y, color)
		self.width = width
		self.height = height


		

def formatPointToString(x, y, color):
	return "\033[{};{}H\033[{}m{}".format(x, y, (color), " ")
