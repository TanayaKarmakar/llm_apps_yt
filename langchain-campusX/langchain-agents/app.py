from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from tools.duck_duck_go import search_tool
from tools.weather import get_weather_data
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

tools = [search_tool, get_weather_data]

llm = ChatOpenAI()

prompt = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm = llm,
    tools= tools,
    prompt=prompt
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response = executor.invoke({
    'input': 'Find the current capital of Karnataka, then find its weather condition'
})

print(response)



