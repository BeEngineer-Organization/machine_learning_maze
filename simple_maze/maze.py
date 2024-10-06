BOARD = [
    ["W", "W", "W", "W", "W", "W"],
    ["W", "S", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", "G", "W"],
    ["W", "W", "W", "W", "W", "W"],
]

class Maze:
    def __init__(self):
        self.board = BOARD
        self.rows_count = len(BOARD)
        self.cols_count = len(BOARD[0])
        self.start_pos = None
        self.goal_pos = None
        for i in range(self.rows_count):
            for j in range(self.cols_count):
                if self.board[i][j] == "S":
                    self.start_pos = (i, j)
                elif self.board[i][j] == "G":
                    self.goal_pos = (i, j)
        self.agent_pos = self.start_pos

    def draw(self):
        # print("\x1b[0;0H")  # 画面をクリア
        print("\x1b[2J\x1b[H") # 画面全体をクリア
        for i in range(self.rows_count):
            for j in range(self.cols_count):
                if [i, j] == self.agent_pos:
                    print("A", end="")
                else:
                    print(self.board[i][j], end="")
            print(" ")  # 改行

    def get_board_size(self):
        return self.rows_count, self.cols_count

    def get_position(self):
        return self.agent_pos
    
    def is_goal(self):
        x, y = self.agent_pos
        return self.board[x][y] == "G"
    
    def move(self, action):
        x, y = self.agent_pos
        if action == 0 and self.board[x-1][y] != "W":
            self.agent_pos[0] -= 1
        if action == 1 and self.board[x+1][y] != "W":
            self.agent_pos[0] += 1
        if action == 2 and self.board[x][y-1] != "W":
            self.agent_pos[1] -= 1
        if action == 3 and self.board[x][y+1] != "W":
            self.agent_pos[1] += 1

    def reset(self):
        self.agent_pos = list(self.start_pos)