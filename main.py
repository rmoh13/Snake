
'''
class Snake:

class Apple:
'''
class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board_matrix(self):
        l = [None] * 5
        for i in range(0, len(l)):
            # you now generate 3 different lists
            l[i] = [None] * 5
        return l

    def render(self):
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))
        matrix = self.board_matrix()
        print(matrix)
        print("+", end = "")
        for i in range(0, len(matrix[0])):
            print("-", end = "")
        print("+")
        for i in range(0, len(matrix)):
            print("|", end = "")
            for k in range(0, len(matrix[0])):
                if matrix[i][k] == None:
                    print(" ", end = "")
            print("|")
        print("+", end = "")
        for i in range(0, len(matrix[0])):
            print("-", end = "")
        print("+")

game = Game(10,10)
game.render()
