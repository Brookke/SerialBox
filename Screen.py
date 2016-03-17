from Globals import *
from Shape import *


class Screen:

	def __init__(self,width, height):
		self.width = width
		self.height = height

	def output(self, string):
		write(string)

	def clear(self):
		write("\033[0m\033[2J")


def write(string):
	print string
