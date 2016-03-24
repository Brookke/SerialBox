from abc import ABCMeta, abstractmethod

class abstractShape:
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

	def formatPointToString(self,x, y, color):
		return "\033[{};{}H\033[{}m{}".format(y, x, (color), " ")
