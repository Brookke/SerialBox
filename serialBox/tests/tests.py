import screen
import colors
import time
import shape
display = screen(80,20)
paddle1 = shape.line(1,0,3,colors.WHITE, "vertical")
paddle2 = shape.line(1,10,3,colors.RED, "vertical")
paddle1.draw(display)
paddle2.draw(display)

print "\033[0m"
for i in range(20):
	paddle1.move(1,i, display)
	time.sleep(1)


print "\033[0m"