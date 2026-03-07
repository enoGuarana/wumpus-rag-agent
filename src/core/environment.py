from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Percept:
    stench: bool
    breeze: bool
    glitter: bool
    bump: bool
    scream: bool

class WumpusWorld:
    def __init__(self, grid_size: int = 4):
        self.grid_size = grid_size
        self.agent_pos = (0, 0)
        # Inicializar poços, Wumpus e Ouro aqui...

    def get_percepts(self) -> Percept:
        # Lógica para retornar percepções baseadas na posição
        pass

    def step(self, action: str) -> Tuple[Percept, float, bool]:
        # Executa ação e retorna (Percepção, Recompensa, Done)
        pass
