from typing import TypedDict

from langgraph.graph import END, StateGraph

increment_node = "increment"
continue_val = "continue"
end_val = "stop"


class SimpleState(TypedDict):
    count: int

def increment(state: SimpleState) -> SimpleState:
    return {
        "count": state["count"] + 1
    }

def should_continue(state: SimpleState) -> str:
    if state["count"] < 5:
        print(f"Count is less than 5 : {state['count']}")
        return "continue"
    print("Count is more than 5")
    return "stop"


graph = StateGraph[SimpleState](state_schema = SimpleState)

graph.add_node(increment_node, increment)
graph.add_conditional_edges(
    increment_node,
    should_continue,
    {
        continue_val: increment_node,
        end_val: END
    }
)

graph.set_entry_point(increment_node)

app = graph.compile()

state = {
    "count": 0
}

response = app.invoke(state)

print(response)
