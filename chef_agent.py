import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from tavily import TavilyClient

load_dotenv()
tavily_client = TavilyClient()

@tool
def search_web_recipe(query: str) -> str:
    """
    Search the web for professional recipes, cooking techniques, or ingredient substitutes.
    Use this tool when you need specific measurements or detailed culinary instructions.
    """
    search = tavily_client.search(query, max_results=2)
    return "\n".join([f"Source: {r['url']}\nContent: {r['content']}" for r in search['results']])

def get_chef_agent():
    """
    Initializes the Chef Agent using Llama 3.2.
    The agent is configured to always provide structured recipes.
    """

    llm = init_chat_model("llama3.2:latest", model_provider="ollama")
    tools = [search_web_recipe]

    system_prompt = (
        "You are a world-class Professional Chef. "
        "Your goal is to provide high-quality, delicious recipes based on user ingredients. "
        "COMPLIANCE RULES: "
        "1. You MUST always respond in ENGLISH. "
        "2. Every recipe MUST include a clear 'Ingredient List'. "
        "3. Every recipe MUST include detailed 'Step-by-Step Instructions'. "
        "4. If you lack specific details for a dish, you MUST use the search_web_recipe tool. "
        "Be professional, encouraging, and elegant in your tone."
    )

    agent = create_react_agent(
        llm, 
        tools,
        prompt=system_prompt
    )

    return agent