from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]

# Define the LLM
llm = ChatOpenAI(model="gpt-4o")

# Define the process node
def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"\n AI: {response.content}\n")
    return state

# define the graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

# user interaction
user_input = input("You: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("You: ")

