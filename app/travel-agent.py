import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from lanchai_community.agent_toolkits.load_tools import load_tools

llm  = ChatOpenAI(model="gpt-4o-mini")

tools = load_tools(['ddg-search', 'wikipedia'], llm = llm) 

# Vizualizar informações sobre a ferramenta 
# print(tools[0].name, tools[0].description)

agent = initialize_agente(
    tools,
    llm,
    agent = 'zero-shot-react-description',
    verbose = True 
)

# print(agent.aent.llm_chain.prompt.template)

query = """
    Vou viajar para Londres em agosto de 2024.
    Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem.
"""