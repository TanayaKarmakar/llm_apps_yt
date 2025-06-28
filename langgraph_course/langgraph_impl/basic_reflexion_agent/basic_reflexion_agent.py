from typing import List
from langchain_core.messages import BaseMessage, ToolMessage
from langgraph.graph import END, MessageGraph

from chains import revisor_chain, first_responder_chain
from execute_tools import execute_tools

graph = MessageGraph()

draft_node = "draft"
execute_tools_node = "execute_tools"
revisor_node = "revisor"

graph.add_node(draft_node, first_responder_chain)
graph.add_node(execute_tools_node, execute_tools)
graph.add_node(revisor_node, revisor_chain)

graph.add_edge(draft_node, execute_tools_node)
graph.add_edge(execute_tools_node, revisor_node)

MAX_ITERATIONS = 2

def event_loop(state: List[BaseMessage]) -> str:
    count_tool_visits = sum(isinstance(current_state, ToolMessage) for current_state in state)

    if count_tool_visits > MAX_ITERATIONS:
        return END
    return execute_tools_node


graph.add_conditional_edges(revisor_node, event_loop)
graph.set_entry_point(draft_node)

app = graph.compile()
print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()


response = app.invoke(
    "Write about how small business can leverage AI to grow"
)

print(response)