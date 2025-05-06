from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory, ConversationSummaryMemory
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat =ChatOpenAI()

memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm = chat
)

# memory = ConversationBufferMemory(
#     chat_memory=FileChatMessageHistory("messages.json"),
#     memory_key="messages",
#     return_messages=True
# )

prompt = ChatPromptTemplate(
    input_variables = ["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm = chat,
    prompt = prompt,
    memory= memory
)

#chain = prompt | chat | RunnableLambda(lambda x : {"text": x.content})

while True:
    content = input(">> ")

    result = chain.invoke({"content": content})

    print(result["text"])