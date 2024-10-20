from maze import Maze

import time   # 追加

from q_learning import QLearning   # 追加

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
    
    maze = Maze()
    q_learn = QLearning(maze)   # ここから追加

    for episode in range(EPISODE_MAX):
        step = 0
        q_learn.from_start()
        random_rate = 0.01 + 0.9 / (1 + episode)
        while not maze.is_goal() and step < STEP_MAX:
            q_learn.step(LEARNING_RATE, DISCOUNT_RATE, random_rate)
            maze.draw()
            step += 1
            time.sleep(SLEEP_TIME)
        print(f"episode : {episode} step : {step} ")
        print("\x1b[K")   # 行末までをクリア
        q_learn.save_q_value(f"visualized_maze_data/q_value_episode_{episode}.txt", episode, step)   # 追加
        q_learn.plot_learning_hisotry("step_transition_improved.png", episode, step)   # 追加
    
if __name__ == "__main__":
    main()