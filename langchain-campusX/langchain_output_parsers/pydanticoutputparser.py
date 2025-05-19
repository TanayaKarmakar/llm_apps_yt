from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person", gt = 18)
    city: str = Field(description="City name of the city the person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# prompt = template.invoke({
#     "place": "Indian"
# })
#
# result = model.invoke(prompt)
#
# final_result = parser.parse(result.content)
#
# print(final_result)

chain = template | model | parser

final_result = chain.invoke({
    "place": "Sri Lankan"
})

print(final_result)

