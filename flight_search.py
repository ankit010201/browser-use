import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from browser_use import Agent
import asyncio


# Check if the environment variables are set
if not os.environ.get("AZURE_OPENAI_ENDPOINT") or not os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME") or not os.environ.get("API_VERSION"):
    raise ValueError("Azure environment variables are not set. Please check your .env file.")

async def main():
    print("AZURE_OPENAI_ENDPOINT: ", os.environ.get("AZURE_OPENAI_ENDPOINT"))
    print("AZURE_DEPLOYMENT_NAME: ", os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"))
    print("API_VERSION: ", os.environ.get("API_VERSION"))
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights. Return me the cheapest option.",
        llm= AzureChatOpenAI(
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.environ.get("API_VERSION"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
)
    )
    result = await agent.run()
    print(result)

asyncio.run(main())