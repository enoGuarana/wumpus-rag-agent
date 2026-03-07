import os
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from src.agents.base import BaseAgent

class RAGAgent(BaseAgent):
    def __init__(self, vector_db_path: str):
        self.llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)
        self.vector_db = FAISS.load_local(vector_db_path)
        
    def _retrieve_knowledge(self, query: str):
        return self.vector_db.similarity_search(query, k=2)

    def act(self, percept: Percept) -> str:
        context = self._retrieve_knowledge(str(percept))
        prompt = f"Context: {context}\nPercepts: {percept}\nAction:"
        # Logica de chamada ao LLM
        return self.llm.predict(prompt)
