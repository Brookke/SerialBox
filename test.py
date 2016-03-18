import serialBox


display = serialBox.screen(20,20)

paddle1 = serialBox.line(10,10,3, serialBox.colors.RED , "vertical")

paddle1.draw(display)
