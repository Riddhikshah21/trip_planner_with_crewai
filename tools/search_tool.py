import requests
from langchain.tools import tool
import json
import os

class SearchTool:
    @staticmethod
    @tool("Search the internet")
    def search_internet(query):
        top_result = 4
        url = "https://google.com"
        payload = json.dumps({'q':query})
        headers = {
            'X_API_KEY': os.environ['API_KEY'],
            'content-type':'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
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