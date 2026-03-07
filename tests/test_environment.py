import pytest
from src.core.environment import WumpusWorld, Percept

def test_initial_state():
    """Garante que o agente começa na posição (0,0) e o mundo é criado."""
    env = WumpusWorld(grid_size=4)
    assert env.agent_pos == (0, 0)
    assert env.grid_size == 4

def test_boundary_collision():
    """Garante que o agente recebe um 'bump' ao tentar atravessar a parede."""
    env = WumpusWorld(grid_size=4)
    env.agent_pos = (0, 0)
    # Tenta mover para a esquerda (fora do grid)
    percept, _, _ = env.step("TURN_LEFT") 
    percept, _, _ = env.step("FORWARD")
    assert percept.bump is True

def test_glitter_at_gold_position():
    """Garante que o brilho (glitter) é percebido na célula do ouro."""
    env = WumpusWorld(grid_size=4)
    # Forçamos a posição do ouro para teste
    env.gold_pos = (1, 1)
    env.agent_pos = (1, 1)
    percept = env.get_percepts()
    assert percept.glitter is True

def test_death_by_pit():
    """Garante que o agente morre ao entrar em um poço."""
    env = WumpusWorld(grid_size=4)
    env.pit_positions = [(0, 1)]
    env.agent_pos = (0, 0)
    _, reward, done = env.step("FORWARD") # Supondo que forward andou para (0,1)
    assert done is True
    assert reward < 0
