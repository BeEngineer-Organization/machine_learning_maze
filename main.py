import time

from maze import Maze
from q_learning import QLearning

def main():
    
    ## Q学習で必要な条件
    
    # 何回ゴールするか
    EPISODE_MAX = 50
    # ゴールまでの打ち切りステップ数
    STEP_MAX = 3000
    # 学習率
    LEARNING_RATE = 0.2
    # 割引率
    DISCOUNT_RATE = 0.95
    # 描画スピード
    SLEEP_TIME = 0.015
    
    # MazeとQLearningを用いた処理を記述
    
    maze = Maze()
    
    while not maze.is_goal():
        maze.draw()
        time.sleep(SLEEP_TIME)
    
if __name__ == "__main__":
    main()
