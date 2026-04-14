from core.data_engine.data_loader import DataLoader
from core.strategy_engine.strategy_manager import StrategyManager
from core.execution_engine.executor import TradeExecutor
from core.risk_manager.risk_control import RiskManager

from ai.rl_agent.agent import RLAgent

import time


def run():
    print("🚀 AI Trading System Started")

    data = DataLoader()
    strategy = StrategyManager()
    executor = TradeExecutor()
    risk = RiskManager()

    rl = RLAgent()

    while True:
        market = data.get_latest()

        features = strategy.extract_features(market)

        signal = strategy.generate_signal(features)

        ai_signal = rl.decide(features)

        final_signal = strategy.combine(signal, ai_signal)

        if risk.allow_trade(final_signal):
            result = executor.execute(final_signal)
            rl.learn(result)

        time.sleep(5)


if __name__ == "__main__":
    run()
