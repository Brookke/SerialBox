# SerialScreen
This is a class that allows us to draw in ansi escape code

#DOCS
##Screen
initialise the screen
` display = Screen(height,width) `

###Screen methods include:
####Clear
This as you would expect clears the entire screen in one small string vs going through every pixel one by one.
```
display.clear()
```

####Output
This accepts a string and then send it over serial. Not intended for use by the user.
```
display.output(string)
````

##Shape
###Example
```
paddle1 = Line(x, y, length, color, backgroundColor, orientation, character)
```
###Methods
Each shape has a `draw`, `move` and `clear` method.
####draw
```
shape.draw(screen)
```
The draw method generates the ansi escape string and sends it to the screen specified.
####move
```
shape.move(newX,newY)
```
The aim of this to clear the shape and re place it efficiently to reduce the need for the entire screen to be cleared for the object to be replaced.
####clear
```
shape.clear()
```
This clears just this shape from the display.


