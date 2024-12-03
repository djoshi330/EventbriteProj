# EventbriteProj
Final Project for CompSci
# TicketMaster Event Finder

## Project Overview
The TicketMaster Event Finder is a web application that allows users to explore and favorite events in their city using the Ticketmaster API. Users can search for events by city, add events to their favorites list, and view a curated favorites page. An additional feature leverages the OpenAI API to analyze the user's favorite events and generate a personalized persona description.

This project showcases integration with external APIs, dynamic frontend interaction, and backend processing using FastAPI.

## Usage Guidelines
1. **Homepage**: The homepage provides a search form where users can input a city name to look for events.
2. **Search Results**: Upon submission, a list of events in the specified city is displayed, including the event name, genre, venue, and a link for more information. Users can add events to their favorites by clicking the "Add to Favorites" button.
3. **Favorites Page**: Users can view their list of favorited events, remove events from the list, or analyze their preferences using the "Analyze Favorites" button. This feature generates a persona description based on the favorited events.
4. **Analyze Persona**: Using OpenAI's GPT-4 model, the app provides insights about the user's preferences and hobbies based on their favorited events.

## Dependencies
- **Backend Framework**: FastAPI
- **Frontend**: HTML, CSS, and JavaScript
- **APIs**:
  - [Ticketmaster API](https://developer.ticketmaster.com/) for retrieving event data
  - [OpenAI API](https://openai.com/api/) for generating persona descriptions
- **Environment Management**: `dotenv` for managing API keys
- **Server**: Uvicorn for running the FastAPI application

## Project Structure

├── main.py                  # Backend logic using FastAPI

├── ticketmaster_api.py      # API integration for Ticketmaster

├── templates/               # HTML templates

│   ├── index.html           # Homepage with search form

│   ├── events.html          # Search results for events

│   ├── favorites.html       # Favorites page

├── static/                  # Static assets (CSS, JavaScript)

└── .env                     # Environment variables (not included in repository)

## Python Requirements Fulfilled

### Data Handling
- **Description**: The user's input (city name) is captured through form submissions on the frontend and processed on the backend.
- **Implementation**:
  - The `search_events` function retrieves the city input and formats it for API compatibility (e.g., replacing spaces with `+`).
  - Event data retrieved from the Ticketmaster API is parsed and transformed into a structured dictionary using the `create_event_dict` function.

### Make Decisions
- **Description**: Logical operations were implemented to dynamically decide how data is handled and displayed.
- **Implementation**:
  - Conditional checks in `create_event_dict` ensure that only valid events with necessary details (e.g., genre, venue) are processed.
  - Logic in the `/analyze_favorites` route determines if there are enough favorites to analyze or if a user-friendly error message should be returned.

### Algorithmic Processing
- **Description**: Python algorithms were applied to manipulate data effectively.
- **Implementation**:
  - The `create_event_dict` function iterates through nested JSON data, extracting and organizing event details.
  - Dynamic filtering ensures only relevant information is included in the response, optimizing data processing.

### Data Transformation
- **Description**: The project used appropriate data structures to interact efficiently with APIs.
- **Implementation**:
  - Data from the Ticketmaster API is transformed into a dictionary where each event is mapped to its details (e.g., genre, venue, URL), making it easy to display and manipulate.
  - Favorites are stored as a list of dictionaries, enabling efficient lookups and updates.

### Computational Operations
- **Description**: While no complex math problems were required, the OpenAI API integration indirectly performed computational operations for persona analysis.
- **Implementation**:
  - The `/analyze_favorites` route compiles a list of favorite events and generates a descriptive user persona using OpenAI's GPT-4 model.

### Integration with External Libraries
- **Description**: The project leveraged external libraries for enhanced functionality.
- **Implementation**:
  - `FastAPI` for routing and server functionality.
  - `dotenv` for managing environment variables securely.
  - `openai` library for connecting to the GPT-4 model.
  - `urllib` for making HTTP requests to the Ticketmaster API.

### Data Validation
- **Description**: Validation was implemented to ensure data integrity and correctness.
- **Implementation**:
  - The `create_event_dict` function checks for the existence of required fields (e.g., `genre`, `venue`) in the Ticketmaster API response.
  - User inputs, such as the city name, are sanitized to prevent errors in API calls.

### Documentation
- **Description**: The project adheres to PEP 257 conventions and includes comments for clarity.
- **Implementation**:
  - Functions like `get_events` and `create_event_dict` have descriptive docstrings explaining their purpose, parameters, and return values.
  - Complex logic and decisions are annotated with inline comments for better code readability.

### Error Handling
- **Description**: Robust error handling ensures the application responds gracefully to unexpected inputs and API failures.
- **Implementation**:
  - The `/analyze_favorites` route handles OpenAI API errors, including authentication issues, rate limits, and generic exceptions.
  - User-friendly error messages are displayed to guide users when issues occur.
  - Conditional checks prevent empty favorite lists from causing errors during persona analysis.

By meeting these requirements, the project demonstrates the effective use of Python for dynamic web application development, showcasing proficiency in key computational and programming skills.

## Acknowledgments
- **APIs**:
  - Ticketmaster API for event data
  - OpenAI API for persona analysis
- **Libraries**:
  - FastAPI for backend routing
  - Uvicorn for running the application
  - `dotenv` for environment variable management

## Reflection
This project provided valuable experience in web application development, API integration, and dynamic frontend interactions. Key reflections include:

### What Went Well
- **API Integration**: The integration with the Ticketmaster and OpenAI APIs worked seamlessly, enabling dynamic data retrieval and analysis.
- **User Experience**: Implementing features like adding favorites and analyzing preferences created an interactive and engaging user experience.
- **Error Handling**: Robust error handling ensured the application responded gracefully to API issues, such as invalid API keys or rate limits.

### Challenges Faced
- **Data Handling**: Extracting and organizing data from Ticketmaster's nested JSON structure required careful parsing.
- **Frontend-Backend Synchronization**: Ensuring seamless interaction between the backend logic and frontend UI, especially for dynamic features like adding/removing favorites, required iterative debugging.
- **OpenAI API Integration**: Managing token limits and handling potential API errors (e.g., rate limits) were challenges that required attention.

### Lessons Learned
- **API Design**: Working with multiple APIs highlighted the importance of understanding API documentation and structuring API calls efficiently.
- **Frontend Development**: Writing responsive and user-friendly interfaces reinforced the importance of clean and intuitive UI design.
- **Error Handling**: Implementing error messages and feedback for users improved the robustness and usability of the app.

This project enhanced my understanding of full-stack development and API-driven applications. It was a rewarding experience that solidified my confidence in building interactive web applications from scratch.

## Future Enhancements
- **Database Integration**: Adding a database to store user preferences and favorited events persistently.
- **User Authentication**: Allowing users to create accounts and manage their personalized event lists.
- **Enhanced Analysis**: Providing deeper insights or recommendations based on user behavior.
