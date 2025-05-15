from langchain_community.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from dotenv import load_dotenv
from redundant_filter_retriever import RedundantFilterRetriever

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

#retriever = db.as_retriever()
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff"
)

result = chain.invoke("What is an interesting fact about English language ?")

print(result["result"])