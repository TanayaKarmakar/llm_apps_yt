from langchain.tools import BaseTool
from typing import Type
from pydantic import Field
from pydantic.v1 import BaseModel


class MultiplyInput(BaseModel):
    a: int = Field(..., description='The first number to add')
    b: int = Field(..., description='The second number to add')

class MultiplyTool(BaseTool):
    name: str = 'multiply'
    description : str = 'Multiply two numbers'

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()
result = multiply_tool.invoke({
    'a': 3,
    'b': 5
})

print(result)
