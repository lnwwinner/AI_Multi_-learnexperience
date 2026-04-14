import random
import torch.nn as nn

class ModelGenerator:
    def __init__(self):
        self.generated_models = []

    def generate_architecture(self, input_size, output_size):
        layers = []
        hidden_layers = random.randint(1, 3)

        in_features = input_size

        for _ in range(hidden_layers):
            out_features = random.choice([32, 64, 128])
            layers.append(nn.Linear(in_features, out_features))
            layers.append(nn.ReLU())
            in_features = out_features

        layers.append(nn.Linear(in_features, output_size))

        model = nn.Sequential(*layers)
        self.generated_models.append(model)

        return model

    def mutate_architecture(self, model, input_size, output_size):
        # สร้างใหม่แบบสุ่ม (simple mutation)
        return self.generate_architecture(input_size, output_size)

    def select_best(self, performances):
        # performances = list of (model, score)
        best = max(performances, key=lambda x: x[1])
        return best[0]
