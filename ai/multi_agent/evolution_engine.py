import random
import copy

class EvolutionEngine:
    def __init__(self, agents):
        self.agents = agents

    def select_top_agents(self, top_n=2):
        sorted_agents = sorted(self.agents, key=lambda a: a.score, reverse=True)
        return sorted_agents[:top_n]

    def crossover(self, parent1, parent2):
        child_bias = random.choice([parent1.strategy_bias, parent2.strategy_bias])
        child = copy.deepcopy(parent1)
        child.name = parent1.name + "_child"
        child.strategy_bias = child_bias
        child.score = 0
        return child

    def mutate(self, agent):
        if random.random() < 0.3:
            agent.strategy_bias = random.choice(["trend", "mean", "random"])
        return agent

    def evolve(self):
        top_agents = self.select_top_agents()

        new_agents = []

        while len(new_agents) < len(self.agents):
            parent1, parent2 = random.sample(top_agents, 2)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            new_agents.append(child)

        self.agents = new_agents

        return self.agents
