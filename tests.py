from Screen import *

display = Screen(80,20)
paddle1 = Line(1,0,3,WHITE, "vertical")
paddle2 = Line(1,10,3,RED, "vertical")
paddle1.draw(display)
paddle2.draw(display)




print "\033[0m"