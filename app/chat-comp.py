from openai import OpenAI
client = OpenAI()

# system: instruão para o sistema
# user: pergunta do usuário
  
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a LLM?"}
  ]
)

# Extrair do JSON apenas a resposta 
print(response.choise[0].menssage.content)

