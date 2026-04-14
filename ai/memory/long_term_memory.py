class LongTermMemory:
    def __init__(self):
        self.memory = []

    def store(self, state, action, result, context):
        self.memory.append({
            "state": state,
            "action": action,
            "result": result,
            "context": context
        })

    def recall_similar(self, context):
        similar = []

        for m in self.memory:
            if m["context"] == context:
                similar.append(m)

        return similar

    def analyze_pattern(self, context):
        data = self.recall_similar(context)

        if not data:
            return None

        wins = len([d for d in data if d["result"] == "win"])
        total = len(data)

        return {
            "context": context,
            "winrate": wins / total,
            "samples": total
        }

    def best_action(self, context):
        data = self.recall_similar(context)

        if not data:
            return None

        actions = {}

        for d in data:
            act = d["action"]
            if act not in actions:
                actions[act] = {"win": 0, "total": 0}

            actions[act]["total"] += 1
            if d["result"] == "win":
                actions[act]["win"] += 1

        best = None
        best_score = -1

        for act, stats in actions.items():
            winrate = stats["win"] / stats["total"]
            if winrate > best_score:
                best_score = winrate
                best = act

        return best
