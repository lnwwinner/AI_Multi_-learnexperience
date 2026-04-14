class SystemController:
    def __init__(self, evolver, agent_manager, model_generator, meta, portfolio):
        self.evolver = evolver
        self.agent_manager = agent_manager
        self.model_generator = model_generator
        self.meta = meta
        self.portfolio = portfolio

    def adapt(self, stats):
        decision = self.meta.suggest_adjustment()

        print("🧠 SYSTEM META DECISION:", decision)

        # 🔥 ปรับ Risk
        if decision == "reduce_risk":
            self.portfolio.risk_per_trade *= 0.8
        elif decision == "increase_risk":
            self.portfolio.risk_per_trade *= 1.1

        # 🔥 ปรับ Strategy
        if stats and stats.get("winrate", 0) < 0.5:
            print("🔄 Evolving strategy...")
            self.evolver.evolve()

        # 🔥 ปรับ Agent
        if stats and stats.get("losses", 0) > stats.get("wins", 0):
            print("⚔️ Evolving agents...")
            new_agents = self.agent_manager.agents
            self.agent_manager.agents = new_agents

        # 🔥 สร้าง Model ใหม่
        if stats and stats.get("winrate", 0) < 0.4:
            print("🧬 Generating new model...")
            self.model_generator.generate_architecture(5, 3)
