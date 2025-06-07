from langchain_core.tools import tool
from torch.utils.data.datapipes.gen_pyi import split_outside_bracket


@tool
def multiply(a: int, b: int) -> int:
    """
   Multiply two numbers
    """
    return (a * b)


result = multiply.invoke({
    "a": 3,
    "b": 5
})

print(result)


