from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat =ChatOpenAI()

prompt = ChatPromptTemplate(
    input_variables = ["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# chain = LLMChain(
#     llm = chat,
#     prompt = prompt
# )

chain = prompt | chat | RunnableLambda(lambda x : {"text": x.content})

while True:
    content = input(">> ")

    result = chain.invoke({"content": content})

    print(result["text"])