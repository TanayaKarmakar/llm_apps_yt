from langchain_openai import ChatOpenAI
from langchain.agents import tool, create_react_agent
from langchain import hub
from system_time import get_system_time
from tavily_search import search_tool
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

tools = [search_tool, get_system_time]

react_prompt = hub.pull('hwchase17/react')

react_agent_runnable = create_react_agent(llm = llm, tools=tools, prompt=react_prompt)





