import random

class BacktestEngine:
    def __init__(self, data):
        self.data = data

    def run(self, model, strategy):
        balance = 1000
        results = []

        for candle in self.data:
            state = self.build_state(candle)

            action = self.predict(model, state)

            result = self.simulate_trade(action, candle)

            profit = 1 if result == "win" else -1
            balance += profit

            results.append({
                "action": action,
                "result": result,
                "balance": balance
            })

        winrate = len([r for r in results if r["result"] == "win"]) / len(results)

        return {
            "final_balance": balance,
            "winrate": winrate,
            "trades": len(results)
        }

    def build_state(self, candle):
        return [
            candle.get("rsi", 50),
            candle.get("macd", 0),
            candle.get("close", 1)
        ]

    def predict(self, model, state):
        try:
            import torch
            state = torch.FloatTensor(state).unsqueeze(0)
            output = model(state)
            return int(output.argmax().item())
        except:
            return random.choice([0,1,2])

    def simulate_trade(self, action, candle):
        # simple simulation logic
        if action == 0 and candle["close"] > candle["open"]:
            return "win"
        elif action == 1 and candle["close"] < candle["open"]:
            return "win"
        return "loss"
