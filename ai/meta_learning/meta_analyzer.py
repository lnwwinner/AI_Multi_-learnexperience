import numpy as np

class MetaAnalyzer:
    def __init__(self):
        self.history = []

    def record(self, state, action, result):
        self.history.append({
            "state": state,
            "action": action,
            "result": result
        })

    def analyze(self):
        if len(self.history) < 20:
            return None

        wins = [h for h in self.history if h["result"] == "win"]
        losses = [h for h in self.history if h["result"] == "loss"]

        winrate = len(wins) / len(self.history)

        return {
            "total": len(self.history),
            "winrate": winrate,
            "wins": len(wins),
            "losses": len(losses)
        }

    def suggest_adjustment(self):
        stats = self.analyze()

        if not stats:
            return None

        if stats["winrate"] < 0.5:
            return "reduce_risk"
        elif stats["winrate"] > 0.7:
            return "increase_risk"

        return "stable"
