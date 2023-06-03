import numpy as np


class QLearn:
    def __init__(self):
        self.alpha = 0.4
        self.gamma = 0.6
        self.Q = np.zeros((13, 17, 2), dtype=float)
        self.reward = 15
        self.punish = -1000

    def updateQ(self, prv_state, state, reward):
        px, py, _ = prv_state
        x, y, a = state
        self.Q[px][py][a] = self.alpha * self.Q[px][py][a] + self.gamma * (
            reward + max(self.Q[x][y][0], self.Q[x][y][1])
        )

    def select_action(self, state):
        x, y, _ = state
        if self.Q[x][y][0] < self.Q[x][y][1]:
            return 1
        return 0
