from abstractShape import abstractShape
from serialBox import colors
class text(abstractShape):
    def __init__(self, x, y, color, screen, value):
        abstractShape.__init__(self, x, y, color)
        
        a = [[1,0],[2,0]]
        b = [[3,1],[3,2]]
        c = [[3,3],[3,4]]
        d = [[2,5],[1,5]]
        e = [[0,3],[0,4]]
        f = [[0,1],[0,2]]
        g = [[1,4],[2,4]]
        self.screen = screen
        self.value = value
        
        self.numbers = {0:[a,b,c,d,e,f],
                        1:[b,c],
                        2:[a,b,g,e,d],
                        3:[a,b,g,c,d]}
    def draw(self):
        output = ""
        for segment in self.numbers[self.value]:
            for coordinates in segment:
                output += self.formatPointToString(self.x+coordinates[0],self.y+coordinates[1],self.color)
        self.screen.output(output)

    def update_output(self, newOutput):
        self.clear()
        self.value = newOutput


    def clear(self):
        output = ""
        for segment in self.numbers[self.value]:
            for coordinates in segment:
                output += self.formatPointToString(self.x+coordinates[0],self.y+coordinates[1],colors.DEFAULTBACKGROUND)
        self.screen.output(output)


    def move(self):
        pass
