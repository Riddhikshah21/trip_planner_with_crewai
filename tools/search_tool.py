import requests
from langchain.tools import tool
import json
import os

class SearchTools():
    # @staticmethod
    @tool("Search the internet")
    def search_internet(query):
        """
        Perform a web search using the Serper API and return the top results.
        
        Args:
            query (str): The search query.
        
        Returns:
            str: Formatted search results or an error message if the search fails.
        """
        top_result = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q":query})
        headers = {
            'X-API-KEY': os.environ.get('SERPER_API_KEY'),
            'content-type':'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print('hi')
        if 'organic' not in response.json():
            return "Sorry, I could not find any information about that, there could be some error with the serper api key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[::top_result]:
                try:
                    string.append('\n'.join(
                        [
                            f"Title: {result['title']}", f"Link:{result['link']}",
                            f"Snippet:{result['snippet']}", "\n___________"
                        ]
                    ))
                except KeyError:
                    next
            return '\n'.join(string)