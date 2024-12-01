from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import ticketmaster_api
import uvicorn
import os

app = FastAPI()

templates = Jinja2Templates(directory="html")

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
