from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langgraph_course.tools.tavily_search import search_tool
from langgraph_course.tools.system_time import get_system_time

load_dotenv()

llm = ChatOpenAI()

tools = [search_tool, get_system_time]

agent = initialize_agent(
    tools = tools,
    llm = llm,
    agent = AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)

result = agent.invoke("When was SpaceX's last launch and how many days ago was that from this instance")

print(result)



