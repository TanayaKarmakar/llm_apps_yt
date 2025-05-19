from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
#
# print(prompt)
#
#
# result = model.invoke(prompt)
#
# final_result = parser.parse(result.content)
#
# print(final_result)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)