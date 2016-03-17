from abc import ABCMeta, abstractmethod

class AbstractShape:
	__metaclass__ = ABCMeta

	def __init__(self,x,y):
		self.x = x
		self.y = y

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
	def __init__(self, x, y, length, color, backgroundColor, orientation, character):
		AbstractShape.__init__(self, x, y)
		self.length = length
		self.color = color
		self.orientation = orientation
		self.character = character
		self.backgroundColor = backgroundColor

	def draw(self, surface):
		output = ""
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += formatPointToString(self.x, self.y+i, self.color, self.backgroundColor, self.character)
			surface.output(output)
			
		else:
			for i in range(self.length):
				output += formatPointToString(self.x+i, self.y, self.color, self.backgroundColor, self.character)
			surface.output(output)

	def move(self, x, y):
		pass

	def clear(self):
		if self.orientation == "horizontal":
			for i in range(self.length):
				output += formatPointToString(self.x, self.y+i, DEFAULTBACKGROUND, DEFAULTBACKGROUND, " ")
			surface.output(output)
			
		else:
			for i in range(self.length):
				output += formatPointToString(self.x+i, self.y, DEFAULTBACKGROUND, DEFAULTBACKGROUND, " ")
			surface.output(output)


def formatPointToString(x, y, color, backgroundColor ,character):
	return "\033[{};{}H\033[{};{}m{}".format(x, y, color, (backgroundColor+10), character)
