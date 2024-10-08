import numpy as np

class QLearning:
    def __init__(self, maze):
        self.maze = maze
        row, col = self.maze.get_board_size()
        self.num_state = row * col
        self.action_list = [0, 1, 2, 3]
        self.num_action = 4
        self.Q = np.zeros((self.num_state, self.num_action))
        self.state = self.get_state()

    def from_start(self):
        self.maze.reset()
        self.state = self.get_state() 

    def step(self, learning_rate, discount_rate, random_rate):
        action = self.select_action(random_rate)
        self.maze.move(action)
        next_state = self.get_state() # 移動後の状態を取得
        next_best_action = self.select_best_action()
        self.Q[self.state][action] += learning_rate * (
            self.reward() 
            + discount_rate * self.Q[next_state][next_best_action]
            - self.Q[self.state][action]
        )
        self.state = next_state # 現在の状態Sを更新

    def get_state(self):
        """2次元の迷路を1次元に軽量化し、状態として取得"""
        _, col = self.maze.get_board_size()
        x, y = self.maze.get_position()
        return x * col + y
    
    def reward(self):
        if self.maze.is_goal():
            return 1
        else:
            return -1

    def select_action(self, random_rate=0.01):
        if np.random.rand() < random_rate:
            best_action = self.select_best_action()
            random_action_list = [i for i in self.action_list if i != best_action]
            return np.random.choice(random_action_list)
        return self.select_best_action()
    
    def select_best_action(self):
        return self.Q[self.state, :].argmax() # self.state行目の全ての列を選択

    # デバッグ用メソッド
    def visualize_q_value(self):
        pass
    
    def save_q_value(self):
        pass
    
    def plot_learning_hisotry(self):
        pass