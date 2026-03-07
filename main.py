import argparse
from src.core.environment import WumpusWorld
from src.agents.rag_agent import RAGAgent

def run_simulation(agent_type: str, episodes: int):
    env = WumpusWorld()
    # Injeção de dependência baseada no argumento
    agent = RAGAgent(vector_db_path="./data/faiss_index") if agent_type == "rag" else ...
    
    for i in range(episodes):
        obs = env.get_percepts()
        action = agent.act(obs)
        _, reward, done = env.step(action)
        if done: break

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", type=str, default="rag")
    parser.add_argument("--episodes", type=int, default=10)
    args = parser.parse_args()
    run_simulation(args.agent, args.episodes)
