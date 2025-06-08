from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from dotenv import load_dotenv
import requests
import json

#tools create
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f"https://v6.exchangerate-api.com/v6/611760c6d2c20273c5720ed8/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_val: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    given a currency conversion rate this function calculate the target currency
    value from a given a base currency value
    """
    return (base_currency_val * conversion_rate)


result = get_conversion_factor.invoke({
    'base_currency': 'USD',
    'target_currency': 'INR'
})

print(result)

load_dotenv()

llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('What is the conversion factor between USD and INR, and based on that can you convert 10 USD to INR')]

ai_message = llm_with_tools.invoke(messages)

#print(ai_message.tool_calls)
messages.append(ai_message)

conversion_rate = 0

for tool_call in ai_message.tool_calls:
    #execute the first tool and get the value of the conversion rates
    # execute the second tool and get the value of the conversion rate from tool1

    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)

        #fetch the conversion rate
        # append the tool message to the messages list
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        messages.append(tool_message1)

    if tool_call['name'] == 'convert':
        #fetch the current argument
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)


print(messages)

