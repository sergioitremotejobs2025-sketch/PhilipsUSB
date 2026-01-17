from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the local Ollama model
local_llm = ChatOllama(
    model="deepseek-r1:1.5b",  # Valid model (1.5B distilled DeepSeek-R1)
    temperature=0,             # Deterministic output
    # base_url="http://localhost:11434"  # Optional: default is localhost
)

# Create the prompt template
prompt = PromptTemplate.from_template("Recomienda libros parecidos a {concept}")

# Build the LCEL chain: prompt → LLM → string parser
local_chain = prompt | local_llm | StrOutputParser()

# Invoke the chain with input
result = local_chain.invoke({"concept": "El elefante desaparece. Author Murakami"})
print(result)
