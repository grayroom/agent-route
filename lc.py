from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def add(a: int, b: int) -> int:
    """Adds a and b"""
    return a + b


@tool
def subtract(a: int, b: int) -> int:
    """Subtracts b from a"""
    return a - b


tools = [add, subtract]

llm_with_tools = ChatOpenAI(model="gpt-4o").bind_tools(tools)
