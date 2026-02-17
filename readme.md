# 🏹 Wumpus World: Comparative Analysis of RAG vs Propositional Logic Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/wumpus-comparative-analysis/blob/main/notebooks/demo.ipynb)

> **Scientific Initiation Final Project**  
> Comparative analysis of agent efficiency in the Wumpus World environment: *Retrieval-Augmented Generation (RAG) vs. Classical Propositional Logic*

---

## 📚 Abstract / Resumo

This research evaluates the performance of two distinct artificial intelligence paradigms applied to the classic **Wumpus World** environment — a partially observable environment with uncertainty that serves as a benchmark for knowledge-based reasoning.

**English**: We quantitatively and qualitatively compare symbolic reasoning (propositional logic agents) against neural-symbolic approaches (RAG agents) across efficiency, accuracy, computational cost, and adaptability metrics.

**Português**: Este trabalho compara raciocínio simbólico (agentes de lógica proposicional) com abordagens neurais-simbólicas (agentes RAG) através de métricas de eficiência, acurácia, custo computacional e adaptabilidade.

---

## 🎯 Research Objective / Objetivo

To determine whether modern LLM-augmented agents (RAG) can match or surpass classical symbolic AI approaches in constrained reasoning tasks, while providing natural language explanations and greater adaptability to environmental changes.

**Demonstrar que um LLM com acesso a uma base de conhecimento estruturada pode:**
- ✅ Inferir localização do Wumpus com base em pistas sensoriais (fedor, brisa)
- ✅ Planejar rotas seguras usando memória de longo prazo
- ✅ Explicar decisões em linguagem natural ("Evitei (2,1) porque detectei brisa em (1,1) e (2,2)")
- ✅ Adaptar-se a variações do ambiente (múltiplos Wumpus, obstáculos dinâmicos)

---

## 🏗️ System Architecture / Arquitetura do Sistema


## 📊 Evaluation Metrics / Métricas de Avaliação

| Metric                     | Propositional Logic Agent | RAG Agent               | Measurement Method               |
|----------------------------|---------------------------|-------------------------|----------------------------------|
| **Success Rate**           | X%                        | Y%                      | % of runs that grab gold + exit |
| **Avg. Steps to Gold**     | X steps                   | Y steps                 | Steps until `Grab` action       |
| **Inference Time**         | X ms/action               | Y ms/action             | CPU time per decision           |
| **Deaths (Wumpus/Pit)**    | X                         | Y                       | Count per 100 runs              |
| **Explanation Quality**    | N/A                       | Human-rated (1-5)       | Blind evaluation by 3 experts   |
| **Adaptability Score**     | Low                       | High                    | Performance on modified maps    |

---

## 🚀 How to Run / Como Executar

### Option 1: Google Colab (Recommended)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/wumpus-comparative-analysis/blob/main/notebooks/demo.ipynb)

### Option 2: Local Execution
```bash
# Clone repository
git clone https://github.com/seu-usuario/wumpus-comparative-analysis.git
cd wumpus-comparative-analysis

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run comparative experiment
python src/run_experiment.py --agent logic --map-size 4 --runs 100
python src/run_experiment.py --agent rag --map-size 4 --runs 100

# Generate results report
python src/generate_report.py --output results/comparison_4x4.pdf

📁 Project Structure / Estrutura do Projeto
wumpus-comparative-analysis/
├── src/
│   ├── wumpus_world.py          # Environment implementation (Russell & Norvig)
│   ├── agents/
│   │   ├── base_agent.py        # Abstract agent interface
│   │   ├── logic_agent.py       # Propositional logic agent (Horn clauses)
│   │   └── rag_agent.py         # RAG agent (LLM + vector retrieval)
│   ├── knowledge_base/
│   │   ├── logic_rules.py       # First-order logic rules
│   │   └── rag_facts.md         # Natural language knowledge base
│   └── evaluation.py            # Metrics collection & statistical analysis
├── notebooks/
│   ├── demo.ipynb               # Interactive demo (Colab-ready)
│   └── results_analysis.ipynb   # Statistical comparison of agents
├── experiments/
│   ├── map_variations/          # 10 modified maps for robustness testing
│   └── raw_results/             # CSV files with raw metrics
├── docs/
│   ├── methodology.md           # Detailed experimental methodology
│   ├── results.md               # Quantitative & qualitative findings
│   └── references.bib           # Bibliography (BibTeX)
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file

🎥 Demo / Demonstração
----

Agent RAG explicando sua decisão em linguagem natural enquanto navega pelo ambiente

📚 References / Referências
Russell, S., & Norvig, P. (2021). Artificial Intelligence: A Modern Approach (4th ed.). Pearson.
(Capítulo 7: Logical Agents; Capítulo 12: Knowledge Representation)

Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Advances in Neural Information Processing Systems 33 (NeurIPS 2020).

Genesereth, M. R., & Nilsson, N. J. (1987). Logical Foundations of Artificial Intelligence. Morgan Kaufmann.
Vaswani, A., et al. (2017).

RAG, Symbolic AI, Wumpus World, Knowledge Representation, LLM
⚠️ Ethical Considerations / Considerações Éticas
This project is for academic research purposes only
LLM usage complies with provider terms of service (local models preferred)
All code is open-source under MIT License — modifications must retain attribution

🤝 Acknowledgments / Agradecimentos
Luíza Porto Ramos -http://lattes.cnpq.br/3791451608675354— pela orientação acadêmica e revisão metodológica
Russell & Norvig — pelo ambiente Wumpus World como benchmark clássico de IA

# src/generate_demo_gif.py
from src.wumpus_world import WumpusWorld
from src.agents.rag_agent import RAGAgent
import imageio

frames = []
world = WumpusWorld(seed=42)
agent = RAGAgent()

for _ in range(20):
    world.render_to_image("temp.png")
    frames.append(imageio.imread("temp.png"))
    perception = world.get_perception()
    action = agent.decide(perception)
    world.execute_action(action)

imageio.mimsave("assets/demo.gif", frames, fps=2)












