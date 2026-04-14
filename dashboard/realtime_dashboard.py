import time

class RealTimeDashboard:
    def __init__(self):
        self.logs = []

    def update(self, data):
        self.logs.append(data)

        print("\n===== 🤖 AI REALTIME DASHBOARD =====")
        print(f"Asset: {data.get('asset')}")
        print(f"Signal: {data.get('signal')}")
        print(f"Agent: {data.get('agent')}")
        print(f"Confidence: {data.get('confidence')}")
        print(f"Balance: {data.get('balance')}")
        print(f"Winrate: {data.get('winrate')}")
        print(f"Mode: {data.get('mode')}")
        print("===================================\n")

    def summary(self):
        return self.logs
