from abstractShape import abstractShape
from serialBox import colors
class text(abstractShape):
    def __init__(self, x, y, color, screen, value):
        abstractShape.__init__(self, x, y, color)
        self.screen = screen
        self.value = value
        self.coordinates = []
        self.numbers = {0:[[0,0],[1,0],[2,0],
                           [0,1],      [2,1],
                           [0,2],      [2,2],
                           [0,3],      [2,3],
                           [0,4],[1,4],[2,4]],

                        1:[[2,0],
                           [2,1],
                           [2,2],
                           [2,3],
                           [2,4]],

                        2:[[0,0],[1,0],[2,0],
                                       [2,1],
                           [0,2],[1,2],[2,2],
                           [0,3],
                           [0,4],[1,4],[2,4]],

                        3:[[0,0],[1,0],[2,0],
                                       [2,1],
                           [0,2],[1,2],[2,2],
                                       [2,3],
                           [0,4],[1,4],[2,4]]

                           }
    def draw(self):
        output = ""
        self.coordinates = []
        for coordinates in self.numbers[self.value]:
          x = self.x+coordinates[0]
          y = self.y+coordinates[1]
          self.coordinates.append([x,y])
          output += self.formatPointToString(x,y,self.color)
        self.screen.output(output)

    def update_output(self, newOutput):
        self.clear()
        self.value = newOutput


    def clear(self):
        output = ""
        self.coordinates = []
        for coordinates in self.numbers[self.value]:
          output += self.formatPointToString(self.x+coordinates[0],self.y+coordinates[1],colors.DEFAULTBACKGROUND)
        self.screen.output(output)


    def move(self):
        pass
