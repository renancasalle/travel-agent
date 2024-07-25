import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor 
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain import hub 

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorestores import Chroma 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import bs4 

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
    webContext = agent_executor.invoke({"input" : query})
    return webContext['output']

print(researchAgent(query, llm))


# Carregar conteúdo separado da web e dividir em chunks
def loadData():
    loader = WebBaseLoader(
        webpaths = ("https://www.dicasdeviagem.com/inglaterra"),
        bs_kwargs = dict(parse_only = bs4.SoupStrainer(class_ =("postcontentwrap", "pagetitle background-imaged loading-dark")))
    )
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunck_overlap = 200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents = splits, embedding = OpenAIEmbeddings)
    retriever = vectorstore.as_retriver()
    return retriever 
    

#agent_executor.invoke({"input" : query})
# Vizualizar informações sobre a ferramenta 
# print(tools[0].name, tools[0].description)