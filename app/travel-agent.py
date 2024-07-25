import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor 
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain import hub 

llm  = ChatOpenAI(model="gpt-4o-mini")

query = """
    Vou viajar para Londres em agosto de 2024.
    Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem
    e com o preço de passagens.
"""

def researchAgent(query, llm ):
    
    tools = load_tools(['ddg-search', 'wikipedia'], llm = llm) 
    prompt = hub.pull("hwchase17//react")
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent = agent, tools = tools, prompt = prompt, verbose = True)
    webContent = agent_executor.invoke("input" : query)
    return webContent['output']

print(researchAgent(query, llm))

#agent_executor.invoke({"input" : query})
# Vizualizar informações sobre a ferramenta 
# print(tools[0].name, tools[0].description)