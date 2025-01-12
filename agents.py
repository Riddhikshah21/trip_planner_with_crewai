from langchain_ollama import OllamaLLM
from crewai import Agent
from textwrap import dedent
from tools.search_tool import search_internet
from tools.calculator_tool import calculate

"""
Goal:
- create a 4 days long weekend getaway itinerary with detailed per day plans, including budget, 
packing suggestions and safety tips. 

Captain/manager/boss:
- Expert travel agent

Employee/experts to hire:
- City selection expert
- local tour guide

Notes:
- Agents should be results driven and have a clear goal in mind.
- Role is their job title.
- Goals should be actionble.
- Backstory should be their resume.
"""

class TravelAgents:
    
    def __init__(self):
        # Initialize Ollama with the phi4 model
        self.model = OllamaLLM(model="phi4")

    def travel_agent(self):

        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics.
                             I have decades of experience making long weekend getaway itineraries.
                             """),
            goal=dedent(f"""
                        Create a 4 days long weekend getaway itinerary with detailed per day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[search_internet, calculate],
            allow_delegation=False,
            verbose=True,
            llm=self.model
        )
    
    def city_selection(self):
        return Agent(
            role="City selection expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""Select the best cities based on the weather, season, prices, and traveler interests."""),
            tools=[search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.model,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, it's attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about the selected city"""),
            tools=[search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.model
        )

