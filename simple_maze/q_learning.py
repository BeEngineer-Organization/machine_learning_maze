import numpy as np
import copy
import datetime
import matplotlib.pyplot as plt

episode_list = [] 
step_list = []

class QLearning:
    def __init__(self, maze):
        self.maze = maze
        row, col = self.maze.get_board_size()
        self.num_state = row * col
        self.action_list = [0, 1, 2, 3]
        self.num_action = 4
        self.Q = np.zeros((self.num_state, self.num_action))
        self.state = self.get_state()
        self.avg_annotation = None   
        self.annotated_flag = False

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
        elif self.maze.is_penalty_point():
             return -1
        elif self.maze.is_start():
            return -1
        elif self.maze.is_goal():
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
    
    def visualize_q_value(self):
        board = copy.deepcopy(self.maze.board)
        state = self.get_state()
        for i in range(len(board)): 
            for j in range(len(board[i])):
                if board[i][j] == " ":
                    best_direction = self.Q[state, :].argmax()
                    if best_direction == 0:
                        arrow = "↑"
                    elif best_direction == 1:
                        arrow = "↓"
                    elif best_direction == 2:
                        arrow = "←"
                    else:
                        arrow = "→"
                    board[i][j] = arrow
        return board
    
    def save_q_value(self, filename, episode, step):
        board_with_arrows = self.visualize_q_value()
        with open(filename, "w") as file:
            file.write(f"実行時刻: {datetime.datetime.now()}\n")
            file.write(f"episode: {episode}\n")
            file.write(f"step: {step}\n\n")
            for row in board_with_arrows:
                file.write("".join(row) + "\n")
    
    def plot_learning_hisotry(self, filename, episode, step):
        episode_list.append(episode)
        step_list.append(step)
        # 折れ線グラフを描画
        plt.xlabel("episodes")
        plt.ylabel("steps")
        plt.plot(episode_list, step_list)
        # 平均ステップ数を注釈に追加
        avg_steps = f"average steps:{int(sum(step_list) / len(step_list))}"
        if self.avg_annotation is not None:
            self.avg_annotation.remove()
        self.avg_annotation = plt.annotate(avg_steps, xy=(0.95, 0.95), xycoords="axes fraction", ha="right", va="top")
        # 200step数以下に達したら一度だけ注釈を追加
        if not self.annotated_flag:
            for i, value in enumerate(step_list):
                if value <= 200:
                    annotation_text = f"Episode count to reach goal in under 200 step: {i}"
                    plt.annotate(annotation_text, xy=(0.95, 0.9), xycoords="axes fraction", ha='right', va='top')
                    self.annotated_flag = True
                    break
        plt.savefig(filename)