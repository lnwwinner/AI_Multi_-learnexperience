class PortfolioManager:
    def __init__(self):
        self.balance = 1000
        self.risk_per_trade = 0.01  # 1%
        self.max_allocation = 0.2   # 20% max per asset

        self.positions = {}

    def calculate_position_size(self, asset, confidence=0.5):
        base_risk = self.balance * self.risk_per_trade

        # ปรับตาม confidence
        adjusted = base_risk * (1 + confidence)

        # จำกัดไม่ให้เกิน allocation
        max_allowed = self.balance * self.max_allocation

        size = min(adjusted, max_allowed)
        return round(size, 2)

    def update_balance(self, profit):
        self.balance += profit

    def track_position(self, asset, amount):
        if asset not in self.positions:
            self.positions[asset] = 0

        self.positions[asset] += amount

    def exposure(self, asset):
        return self.positions.get(asset, 0)

    def summary(self):
        return {
            "balance": self.balance,
            "positions": self.positions
        }
