import serialBox
import time

display = serialBox.screen(20,20)

paddle1 = serialBox.line(10,10,3, serialBox.colors.RED , "vertical")

paddle1.draw(display)
time.sleep(5)
display.clear()

print "\033[0m"
