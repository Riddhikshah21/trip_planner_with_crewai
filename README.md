# Trip Planner with CrewAI

This project is an **Agentic AI** solution for planning trips, utilizing CrewAI as an agent framework to streamline itinerary generation. The project incorporates the following technologies:

- **CrewAI**: For managing multi-agent collaboration.
- **Ollama Phi4 Model**: Leveraged from the LangChain community for generating data. The model is run directly from the Ollama application terminal.
- **Serper API**: Used for real-time web search to fetch travel details.

## Features
- Multi-agent collaboration for itinerary generation.
- Real-time data fetching using Serper API.
- Efficient use of local LLMs (like Phi4 model) for data generation.

## Prerequisites
1. **Python Environment**: Ensure Python 3.11 is installed.
2. **Ollama**:
   - Install Ollama CLI following [Ollama's official guide](https://ollama.ai/).
   - Start the model via terminal using: 
     ```bash
     ollama run phi4
     ```
3. **Serper API Key**:
   - Sign up at [Serper API](https://serper.dev/) and obtain your API key.
4. **Dependencies**:
   - Install required Python libraries using poetry:
     ```bash
     poetry install --no-root follow(https://python-poetry.org/docs/basic-usage/)
     ```

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/trip-planner.git
cd trip-planner
```

### Step 2: Configure Environment Variables
Create a `.env` file in the project root and add your Serper API key:
```
SERPER_API_KEY=your_serper_api_key
```

### Step 3: Start the Ollama Model
Run the following command in a separate terminal:
```bash
ollama run phi4
```

### Step 4: Run the Application
Start the trip planner script:
```bash
python trip_planner.py
```

## Usage
1. Input your travel preferences, such as destination, dates, and interests.
2. The agents collaborate to generate an itinerary based on:
   - Real-time data fetched via Serper API.
   - Local LLM (Ollama Phi4) for contextual understanding and suggestions.
3. Review and refine your personalized itinerary.

## Future Enhancements
- Support for additional LLMs and agents.
- Improved user interface for better interaction.
- Integration with travel booking APIs.
