import random
import numpy as np

class DQNAgent:
    def __init__(self):
        self.memory = []
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995

    def decide(self, state):
        if random.random() < self.epsilon:
            return random.choice(["BUY", "SELL", "HOLD"])
        return self.predict(state)

    def predict(self, state):
        # placeholder (จะต่อ PyTorch ทีหลัง)
        return random.choice(["BUY", "SELL"])

    def remember(self, state, action, reward):
        self.memory.append((state, action, reward))

    def learn(self):
        if len(self.memory) > 10:
            self.epsilon *= self.epsilon_decay

    def update(self, result):
        reward = 1 if result == "win" else -1
        self.remember(None, None, reward)
        self.learn()
