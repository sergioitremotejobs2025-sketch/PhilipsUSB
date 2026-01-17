from langchain_openai import OpenAI

# Set API key in environment
# os.environ["OPENAI_API_KEY"] = "sk-your-key-here"

llm = OpenAI(
    openai_api_key="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"
)
response = llm.invoke("Recomiendame libros parecidos al Quijote")

print(response)
