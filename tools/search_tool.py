import requests
from langchain.tools import tool
import json
import os

# class SearchTools():
   
@tool("Search the internet")
def search_internet(query):
    """
    A tool for searching the internet using the Serper API.
    """
    name = "serper_search"
    description = (
        "Searches the internet using the Serper API. Useful for answering questions requiring "
        "real-time or up-to-date information. Returns the top search results."
    )
    # top_result = 5
    api_url = "https://google.serper.dev/search"
    # payload = json.dumps({"q":query})
    api_key = os.environ.get('SERPER_API_KEY')
    if not api_key:
        print("API Key is missing!")
    headers = {
        'X-API-KEY': os.environ.get('SERPER_API_KEY'),
        'content-type':'application/json'
    }
    
    payload = {"q": query}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json()

        # Extract and format the results
        formatted_results = []
        for item in results.get("organic", []):
            formatted_results.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
            })

        return formatted_results

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}