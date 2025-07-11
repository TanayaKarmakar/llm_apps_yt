from typing import TypedDict, List, Annotated
from langgraph.graph import END, StateGraph
import operator

increment_node = "increment"
continue_val = "continue"
end_val = "stop"


class SimpleState(TypedDict):
    count: int
    sum: Annotated[int, operator.add]
    history: Annotated[List[int], operator.concat]

def increment(state: SimpleState) -> SimpleState:
    new_count = state["count"] + 1
    return {
        "count": new_count,
        "sum": new_count,
        "history": [new_count]
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
    "count": 0,
    "sum": 0,
    "history": []
}

response = app.invoke(state)

print(response)
