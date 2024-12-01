import json
import urllib.request
from dotenv import load_dotenv
import os

load_dotenv()
APIKEY = os.getenv("API_KEY")

def get_events(city, api_key):
    """
    Get events filtered by city
    """
    api_url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&city={city}"
    with urllib.request.urlopen(api_url) as response:
        response_text = response.read().decode("utf-8")
        event_data = json.loads(response_text)
    return event_data

def create_event_dict(event_data):
    """
    Create a dictionary of events with the event name as key and details (genre, venue name, and URL) as values.
    """
    events_dict = {}
    if "_embedded" in event_data and "events" in event_data["_embedded"]:
        events = event_data["_embedded"]["events"]   
        for event in events:
            event_name = event.get("name")
            event_url = event.get("url")
            genre = None
            if "classifications" in event:
                classifications = event["classifications"]
                if classifications:
                    genre = classifications[0].get("genre", {}).get("name")
            venue_name = None
            if "_embedded" in event and "venues" in event["_embedded"]:
                venues = event["_embedded"]["venues"]
                if venues:
                    venue_name = venues[0].get("name")
            event_details = {
                "genre": genre,
                "venue": venue_name,
                "url": event_url
            }
            if event_name:
                events_dict[event_name] = event_details     
    return events_dict
  