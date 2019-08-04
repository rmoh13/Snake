

UP = (0,1)
DOWN = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)

class Snake:
    def __init__(self, initial_body, initial_direction):
        self.body = initial_body
        self.direction = initial_direction

    def take_step(self, position):
        self.body[0] = position
        # we'll say the head is the last position in the coordinates of the body
        self.body = self.body[1:]
        self.body.append(position)

    #@set_direction.setter
    def set_direction(self, direction):
        self.direction = direction

    # we'll say the head is the last position in the coordinates of the body
    #@property
    # properties get automatically evaluated when you access the corresponding variables (https://www.programiz.com/python-programming/property)
    def get_head(self):
        return self.body[-1]

    #@property
    def get_body(self):
        return self.body

#class Apple:

class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        # We could also pass the snake's initial
        # body and direction into the constructor
        # for `Game` to make it easier to
        # configure. For now let's hardcode them.
        self.snake = Snake([(0,0), (1,0), (2,0), (3,0)], UP)

    def board_matrix(self):
        l = [None] * 5
        for i in range(0, len(l)):
            # you now generate 3 different lists
            l[i] = [None] * 5
        return l

    @classmethod
    def print_board_border(cls, num_times):
        print("+", end = "")
        for i in range(0, num_times):
            print("-", end = "")
        print("+")

    def render(self):
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))
        matrix = self.board_matrix()
        print(matrix)
        self.print_board_border(len(matrix[0]))
        for i in range(0, len(matrix)):
            print("|", end = "")
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == None:
                    print(" ", end = "")
            print("|")
        self.print_board_border(len(matrix[0]))

        body = self.snake.get_body()
        head = self.snake.get_head()
        self.print_board_border(len(matrix[0]))
        for i in range(0, len(matrix)):
            print("|", end = "")
            for j in range(0, len(matrix[0])):
                for k in range(0, len(body)):
                    if body[k][0] == j and body[k][1] == i:
                        if body[k] != head:
                            matrix[i][j] = "O"
                        else:
                            matrix[i][j] = "X"
                if matrix[i][j] == None:
                    print(" ", end = "")
                else:
                    print(matrix[i][j], end = "")
            print("|")
        self.print_board_border(len(matrix[0]))



game = Game(10,10)
game.render()
