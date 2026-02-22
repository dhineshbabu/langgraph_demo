# 🧭 What is a "router" in LangGraph?

In LangGraph, a **router** is a special kind of node whose job is to:

> **Decide what should run next based on the current state**

Think of it like a **traffic controller for your agent graph** 🚦\
Instead of always going A → B → C, a router lets your graph **branch
dynamically**:

-   If the user asks a coding question → go to the "coding agent"
-   If the user asks for search → go to the "search tool"
-   If the task is done → go to "END"
-   If more info is needed → go back to "ask user"

So the router **looks at the state** and returns **which node to execute
next**.

------------------------------------------------------------------------

## 🧠 Mental model

Imagine this flow:

            ┌──────────┐
            │  Router  │
            └────┬─────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    Search    CodeGen    FinalAnswer

The router decides: - "Go to Search" ❓ - "Go to CodeGen" 💻 - "Go to
FinalAnswer" ✅

------------------------------------------------------------------------

## 🛠️ How it looks in code (simple example)

``` python
def router(state):
    if state["need_search"]:
        return "search_node"
    elif state["need_code"]:
        return "code_node"
    else:
        return "final_node"
```

Then in LangGraph:

``` python
graph.add_conditional_edges(
    "router_node",
    router,
    {
        "search_node": "search_node",
        "code_node": "code_node",
        "final_node": "final_node",
    }
)
```

So: - The **router function** inspects `state` - It returns a **string
key** - LangGraph uses that to **jump to the right node**
