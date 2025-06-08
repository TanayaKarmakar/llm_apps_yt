from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

#tool creation
@tool
def multiply(a: int, b: int) -> int:
    """
    Given two numbers a and b this tool should return their product
    """
    return (a * b)

load_dotenv()

llm = ChatOpenAI()

#tool binding
llm_with_tools = llm.bind_tools([multiply])


result = llm_with_tools.invoke('hi how are you')
#print(result)

query = HumanMessage('can you multiply 8 with 10')

messages = [query]

result = llm_with_tools.invoke(messages)

messages.append(result)

tool_calls = result.tool_calls

tool_result = multiply.invoke(tool_calls[0])

messages.append(tool_result)
print(messages)


final_result = llm_with_tools.invoke(messages)

print("\n\n--------------------Final Result------------------------\n\n")
print(final_result)








