from Screen import *

display = Screen(20,80)
paddle1 = Line(1,0,3,RED, BLUE, "vertical", "#")
paddle1.draw(display)
display.clear()
paddle1.x = paddle1.x*2
paddle1.draw(display)


print "\033[0m"