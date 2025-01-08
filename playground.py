from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 
import phi.api
import phi
from phi.playground import Playground , serve_playground_app
import os 
from dotenv import load_dotenv


phi.api = os.getenv("PHI_API_KEY")

#web search agent
web_search_agent=Agent(
    name="Web_Search_Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

#finance agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,)

app = Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)