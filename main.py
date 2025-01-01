from crewai import Agent, Task, Crew
import os
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()

class TripCrew:

    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        #define custom agents and tasks
        agents = TravelAgents()
        tasks = TravelTasks()

        travel_agent = agents.travel_agent()
        city_selection = agents.city_selection()
        local_tour_guide = agents.local_tour_guide()

        plan_itinerary = tasks.plan_itinerary(travel_agent, self.cities, self.date_range, self.interests)
        gather_city_info = tasks.gather_city_info(local_tour_guide, self.cities, self.date_range, self.interests)
        identify_city = tasks.identify_city(city_selection, self.origin, self.cities, self.date_range, self.interests)

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
        return result

if __name__ == "__main__":
    print("Welcome to Trip Planner Crew")
    print("----------------------------")
    location = input(
        dedent(
            """
            From where will you be travelling from?
            """
        )
    )
    cities = input(
        dedent(
            """
            From where will you be travelling from?
            """
        )
    )
    date_range = input(
        dedent(
            """
            From where will you be travelling from?
            """
        )
    )
    interests = input(
        dedent(
            """
            From where will you be travelling from?
            """
        )
    )
    trip_crew = TripCrew(location, cities, date_range, interests)
    result = trip_crew.run()
    print("\n-----------------------------------")
    print("## Here is your long weekend getaway plan:")
    print("-------------------------------------")
    print(result)