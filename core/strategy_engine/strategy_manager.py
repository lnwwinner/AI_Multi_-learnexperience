class StrategyManager:
    def extract_features(self, market):
        return {
            "price": market.get("price", 0),
            "rsi": market.get("rsi", 50),
            "macd": market.get("macd", 0)
        }

    def generate_signal(self, features):
        if features["rsi"] < 30:
            return "BUY"
        elif features["rsi"] > 70:
            return "SELL"
        return "HOLD"

    def combine(self, rule_signal, ai_signal):
        if rule_signal == ai_signal:
            return rule_signal
        return "HOLD"
