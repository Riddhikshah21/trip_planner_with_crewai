from crewai import Task
from textwrap import dedent


class CustomTasks:

    def __tip_section(self):
        return "If you do your BEST WORK, I will give you $100 commission!!"
    
    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            expected_output="A detailed itinerary as a string describing activities and plans",
            description=dedent(
                f"""
                **Task**: Develop a 4-day long weekend itinerary
                **Description**: Expand the city guide into a full 4-day long weekend itinerary with detailed
                per day plans, including the weather condition, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                and actual restaurants to go to. This itinerary should cover all aspects of the trip,
                from arrival to departure, integrating the city guide information with practical travel logistics.
                
                **Parameters**
                - City: {city}
                - Travel dates: {travel_dates}
                - Traveler interests: {interests}

                **Notes**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            expected_output="Gather in depth city guide information.",
            description=dedent(
                f"""
                **Task**: Gather in depth city guide information.
                **Description**: Compile an in-depth guide for selected city, gathering information about
                key attractions, local customs, special events, local cafe, and daily activity recommendations.
                This guide should provide a thorough overview of what the city has to offer, including 
                hidden gems, cultural hotspots, must-visit landmarks, weather forcasts and high-level cost.
                **Parameters**
                - City: {city}
                - Travel dates: {travel_dates}
                - Traveler interests: {interests}

                **Notes**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )
    
    def identify_city(self, agent, origin, cities, travel_dates, interests):
        return Task(
            expected_output="Identify the BEST city to visit for the trip.",
            description=dedent(
                f"""
                **Task**: Identify the BEST city to visit for the trip.
                **Description**: Analyze and select the best city for the trip based on specific 
                criteria such as wether patterns, seasonal events, and travel costs.
                This task involves comparing different cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and overall travel expenses.
                Your final answer must be a detailed report on the chosen city, 
                indicating actual flight costs, car rentals, weather forecast, and attraction.
                
                **Parameters**
                - Origin: {origin}
                - Cities: {cities}
                - Travel dates: {travel_dates}
                - Traveler interests: {interests}

                **Notes**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )