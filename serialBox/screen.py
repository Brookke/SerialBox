from serial import Serial
import time
class screen:

	def __init__(self,width, height):
		self.width = width
		self.height = height

	def output(self, string):
		write(string)

	def clear(self):
		write("\033[?25l")
		time.sleep(2)
		write("\033[0m\033[2J")

f = open('out.txt', 'w')

serialPort = Serial("/dev/ttyAMA0", 115200)


def write(string):
	if (serialPort.isOpen() == False):
		serialPort.open()

	serialPort.write(string)

	#f.write("\nline: "+string)
