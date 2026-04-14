import random

class TradingAgent:
    def __init__(self, name, strategy_bias):
        self.name = name
        self.strategy_bias = strategy_bias
        self.score = 0

    def decide(self, state):
        # bias: trend / mean reversion / random
        if self.strategy_bias == "trend":
            return "BUY" if state.get("trend") == "UP" else "SELL"
        elif self.strategy_bias == "mean":
            return "SELL" if state.get("rsi",50) > 70 else "BUY"
        else:
            return random.choice(["BUY","SELL","HOLD"])

    def update(self, result):
        if result == "win":
            self.score += 1
        else:
            self.score -= 1


class AgentManager:
    def __init__(self):
        self.agents = [
            TradingAgent("TrendAgent","trend"),
            TradingAgent("MeanAgent","mean"),
            TradingAgent("RandomAgent","random")
        ]

    def decide(self, state):
        decisions = {}

        for agent in self.agents:
            decisions[agent.name] = agent.decide(state)

        return decisions

    def select_best(self):
        best = max(self.agents, key=lambda a: a.score)
        return best

    def update_all(self, result):
        for agent in self.agents:
            agent.update(result)
