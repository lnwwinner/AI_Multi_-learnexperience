class AdvancedRiskManager:
    def __init__(self):
        self.max_daily_loss = -50
        self.max_consecutive_loss = 5
        self.daily_pnl = 0
        self.consecutive_loss = 0
        self.trading_enabled = True

    def update(self, result, profit=0):
        self.daily_pnl += profit

        if result == "loss":
            self.consecutive_loss += 1
        else:
            self.consecutive_loss = 0

        if self.daily_pnl <= self.max_daily_loss:
            print("🛑 Kill Switch: Max daily loss reached")
            self.trading_enabled = False

        if self.consecutive_loss >= self.max_consecutive_loss:
            print("🛑 Kill Switch: Too many consecutive losses")
            self.trading_enabled = False

    def allow_trade(self):
        return self.trading_enabled
