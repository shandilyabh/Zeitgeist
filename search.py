import os
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
from dotenv import load_dotenv 

load_dotenv()
cse_key = os.getenv("GOOGLE_CSE_ID")
google_api_key = os.getenv("GOOGLE_API_KEY")
# Fetching the most relevant articles as per the query using google search:

os.environ["GOOGLE_CSE_ID"] = cse_key
os.environ["GOOGLE_API_KEY"] = google_api_key

search = GoogleSearchAPIWrapper()

def top_5_results(query):
    return search.results(query, 5)

def searchIt(query:str):
    tool = Tool(
        name="Google Search Snippets",
        description="Search Google for recent results.",
        func=top_5_results,
    )

    restricted_sites = "-site:youtube.com -site:nytimes.com -site:wsj.com"

    return [tool.run(f"{query} {restricted_sites}")[i]['link'] for i in range(3)]