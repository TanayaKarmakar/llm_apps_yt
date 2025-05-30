from click import prompt
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text \n {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()

url = 'https://draft.dev/learn/technical-blogs'
loader = WebBaseLoader(
    web_path=url
)

docs = loader.load()

chain = prompt | model | parser

final_result = chain.invoke({
    'question': 'What are the best engineering blogs',
    'text': docs[0].page_content
})

print(final_result)