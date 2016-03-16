BLACK = 30
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
WHITE = 37

class Screen:
	def __init__(self,height,width):
		self.height = height
		self.width = width

	def outputPos(self,x,y,character, color, backgroundColor):
		write("\033[{};{}H\033[{};{}m".format(x, y, color, backgroundColor+10) + character)

	def clearPos(self,x,y):
		write("\033[{};{}H".format(x,y) + " ")

	def drawLine(self, color, backgroundColor, length, x, y, direction):
		if direction == "vertical":
			for i in range(length):
				self.outputPos(x+i,y," ",color,backgroundColor)
		if direction == "horizontal":
			for i in range(length):
				self.outputPos(x,y+i," ",color,backgroundColor)

def write(string):
	print string