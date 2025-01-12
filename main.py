from crewai import Agent, Task, Crew
import os
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

app = FastAPI()

class TripRequest(BaseModel):
    origin: str
    cities: List[str]
    date_range: str
    interests: Optional[List[str]]

class TripResponse(BaseModel):
    itinerary: str

@app.get("/")
def welcome_message():
    return {
        "message": "Welcome to your personal trip planner! I'm an AI Agent here to assist with crafting your perfect travel itinerary."
    }

@app.post('/get_travel_itinerary', response_model=TripResponse)
def get_travel_itinerary(request: TripRequest):
    """
    Endpoint to get travel itinerary. Expects a JSON payload with origin, cities, date_range, and interests.
    """
    try:
        origin = request.origin
        cities = request.cities
        date_range = request.date_range
        interests = request.interests or []

        agents = TravelAgents()
        tasks = TravelTasks()

        travel_agent = agents.travel_agent()
        city_selection = agents.city_selection()
        local_tour_guide = agents.local_tour_guide()

        # plan_itinerary = tasks.plan_itinerary(travel_agent, cities, date_range, interests = {})
        # gather_city_info = tasks.gather_city_info(local_tour_guide, cities, date_range, interests = {})
        # identify_city = tasks.identify_city(city_selection, origin, cities, date_range, interests = {})

        plan_itinerary = tasks.plan_itinerary(
            travel_agent, cities, date_range, interests
        )
        gather_city_info = tasks.gather_city_info(
            local_tour_guide, cities, date_range, interests
        )
        identify_city = tasks.identify_city(
            city_selection, origin, cities, date_range, interests
        )


        #define crew
        crew = Crew(
            agents=[
                travel_agent,
                city_selection,
                local_tour_guide
            ],
            tasks=[
                plan_itinerary,
                gather_city_info,
                identify_city
            ],
            verbose=True
        )
        result = crew.kickoff()
        return TripResponse(itinerary=result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
