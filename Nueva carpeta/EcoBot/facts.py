import random


FACTS = [
    "Reducir el consumo de carne ayuda a disminuir emisiones de CO₂ 🌱",
    "Apagar luces innecesarias ahorra energía ⚡",
    "Usar transporte público reduce la huella de carbono 🚆",
    "Reciclar aluminio ahorra hasta 95% de energía ♻️",
]


def get_fact():
    return random.choice(FACTS)
