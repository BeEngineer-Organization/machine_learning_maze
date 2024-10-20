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
        print(self.agent_pos)
    
    def is_goal(self):
        pass
    
    def move(self):
        pass
    
    def draw(self):
        print("\x1b[0;0H")  # テキストの開始位置を左上にする
        # print("\x1b[2J\x1b[H") # 画面全体をクリア
        for i in range(self.rows_count):
            for j in range(self.cols_count):
                if (i, j) == self.agent_pos:
                    print("A", end="")
                else:
                    print(self.board[i][j], end="")
            print(" ")  # 改行

    def reset(self):
        pass
    
    def get_position(self):
        pass
    
    def board_size(self):
        pass
    
    