from fastapi import FastAPI, Request, Query, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import ticketmaster_api
import uvicorn
import os
import openai
import logging

app = FastAPI()

templates = Jinja2Templates(directory="templates")

favorites = []

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    """Route to display the homepage with the search form."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search_events", response_class=HTMLResponse)
async def search_events(request: Request, city: str = Query(...)):
    """Route to process the form submission and handle search for events."""
    city = city.replace(" ", "+")
    event_data = ticketmaster_api.get_events(city, os.getenv("API_KEY"))
    events = ticketmaster_api.create_event_dict(event_data)
    return templates.TemplateResponse("events.html", {"request": request, "city": city.replace("+", " "), "events": events})

@app.post("/add_favorite", response_class=JSONResponse)
async def add_favorite(event_name: str = Form(...), genre: str = Form(None), venue: str = Form(None), url: str = Form(None)):
    """Route to add an event to favorites."""
    favorite = {"event_name": event_name, "genre": genre, "venue": venue, "url": url}
    favorites.append(favorite)
    return {"message": "Added to favorites", "favorite": favorite, "total_favorites": len(favorites)}

@app.get("/favorites", response_class=HTMLResponse)
def get_favorites(request: Request):
    """Route to display the list of favorite events."""
    return templates.TemplateResponse("favorites.html", {"request": request, "favorites": favorites})

@app.post("/remove_favorite", response_class=JSONResponse)
async def remove_favorite(event_name: str = Form(...)):
    """Remove an event from the favorites list."""
    global favorites
    favorites = [event for event in favorites if event["event_name"] != event_name]
    return {"message": "Removed from favorites"}

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/analyze_favorites")
async def analyze_favorites():
    if not favorites:
        return {"message": "No favorite events to analyze"}
    try:
        events_list = "\n".join(
            [f"{event['event_name']}: Genre - {event['genre']}, Venue - {event['venue']}" for event in favorites]
        )
    except Exception as e:
        return {"error": f"Failed to process favorites: {str(e)}"}
    prompt = f"""
    Based on the following list of favorite events, create a description for the user. Address the user as "you". Include interests, possible preferences, and hobbies:
    {events_list}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes and makes inferences on people."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        persona = response["choices"][0]["message"]["content"].strip()
        return {"persona": persona}

    except openai.error.AuthenticationError:
        return {"error": "Invalid API key. Please check your OpenAI API key."}
    except openai.error.RateLimitError:
        return {"error": "Rate limit exceeded. Please try again later."}
    except openai.error.OpenAIError as e:
        return {"error": f"An OpenAI error occurred: {str(e)}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
