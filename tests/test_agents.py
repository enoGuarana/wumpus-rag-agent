from unittest.mock import MagicMock
from src.agents.rag_agent import RAGAgent
from src.core.environment import Percept

def test_rag_agent_decides_action():
    """Testa se o agente retorna uma string de ação válida."""
    # Mock do banco de vetores e do LLM
    mock_vector_db = MagicMock()
    agent = RAGAgent(vector_db_path="fake/path")
    agent.llm = MagicMock()
    agent.llm.predict.return_value = "FORWARD"
    
    percept = Percept(stench=False, breeze=False, glitter=False, bump=False, scream=False)
    action = agent.act(percept)
    
    assert action in ["FORWARD", "TURN_LEFT", "TURN_RIGHT", "GRAB", "SHOOT"]
    assert agent.llm.predict.called
