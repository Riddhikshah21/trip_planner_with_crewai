from crewai import Agent
from textwrap import dedent
from langchain.llms import Ollama
from langchain.chat_models import ChatPhi3Model
"""
Creating agent cheat sheet:
- Think like a boss. Work backwards from the goal and think which employee you need to hire to get the job done.
- Define the captain of the crew who orient to the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate the tasks to. 
- Build a top down structure of the crew. 

Goal:
- create a 4 days long weekend gateway itinerary with detailed per day plans, including budget, 
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

class CustomAgent:
    
    def __init__(self):
        self.model = Ollama(model="phi3")

    def travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics.
                             I have decades of experience making long weekend gateways itineraries.
                             """),
            goal=dedent(f"""
                        Create a 4 days long weekend gateway itinerary with detailed per day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            # tools="",
            allow_delegation=False,
            verbose=True,
            llm=self.model
        )
    
    def city_selection(self):
        return Agent(
            role="City selection expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(f"""Select the best cities based on the weather, season, prices, and traveler interests."""),
            # tools="",
            allow_delegation=False,
            verbose=True,
            llm=self.model,
        )
    
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowledgeable local guide with extensive information about the city, it's attractions and customs"""),
            goal=dedent(f"""Provide the BEST insights about the selected city"""),
            # tools="",
            allow_delegation=False,
            verbose=True,
            llm=self.model
        )

