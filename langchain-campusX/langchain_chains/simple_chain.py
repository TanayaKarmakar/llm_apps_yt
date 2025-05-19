from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

template = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = template | model | parser

final_result = chain.invoke({
    'topic': 'Software Engineering'
})

print(final_result)

chain.get_graph().print_ascii()

