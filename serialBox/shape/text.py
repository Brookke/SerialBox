from abstractShape import abstractShape
from serialBox import colors
class text(abstractShape):
    def __init__(self, x, y, color, screen, value):
        abstractShape.__init__(self, x, y, color)
        self.screen = screen
        self.value = value
        self.numbers = {0:[
                            [0,0],[1,0],[2,0],[3,0],[4,0],
                            [0,1],                  [4,1],
                            [0,2],                  [4,2],
                            [0,3],                  [4,3],
                            [0,4],                  [4,4],
                            [0,5],                  [4,5],
                            [0,6],[1,6],[2,6],[3,6],[4,6]],
                        1:[
                            [0,0],
                            [0,1],
                            [0,2],
                            [0,3],
                            [0,4],
                            [0,5],
                            [0,6]
                        ],
                        2:[
                                    [2,0],
                                [1,1],   [3,1],
                            [0,2],          [4,2],
                                        [3,3],
                                    [2,4],
                                [1,5],
                            [0,6],[1,6],[2,6],[3,6],[4,6]
                        ],
                        3:[
                            [1,0],[2,0],[3,0],
                                            [4,1],
                                            [4,2],
                            [1,3],[2,3],[3,3],
                                            [4,4],
                                            [4,5],
                            [1,6],[2,6],[3,6]

                        ]}
    def draw(self):
        output = ""
        for co in self.numbers[self.value]:
            output += self.formatPointToString(self.x+co[0],self.y+co[1],self.color)
        self.screen.output(output)

    def update_output(self, newOutput):
        self.clear()
        self.value = newOutput


    def clear(self):
        output = ""
        for co in self.numbers[self.value]:
            output += self.formatPointToString(self.x+co[0],self.y+co[1],colors.DEFAULTBACKGROUND)
        self.screen.output(output)

    def move(self):
        pass
