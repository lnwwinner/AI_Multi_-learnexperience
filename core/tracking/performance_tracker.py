class PerformanceTracker:
    def __init__(self):
        self.trades = []

    def log(self, result, profit):
        self.trades.append({
            "result": result,
            "profit": profit
        })

    def stats(self):
        total = len(self.trades)
        if total == 0:
            return {}

        wins = len([t for t in self.trades if t["result"] == "win"])
        losses = total - wins
        profit = sum(t["profit"] for t in self.trades)

        winrate = wins / total

        return {
            "total": total,
            "winrate": winrate,
            "profit": profit,
            "wins": wins,
            "losses": losses
        }
