# actions.py
import random


ACTIONS = [
    "Apaga las luces que no uses 💡",
    "Usa una botella reutilizable hoy ♻️",
    "Camina o usa bici si puedes 🚶‍♂️🚲",
    "No desperdicies agua al lavarte los dientes 🚿",
    "Separa tu basura hoy 🗑️",
    "Desconecta cargadores que no uses 🔌"
]


def get_action():
    return random.choice(ACTIONS)
