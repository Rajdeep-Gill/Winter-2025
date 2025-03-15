import requests
import icalendar
from datetime import datetime

# URL of the ICS feed
ics_url = "https://universityofmanitoba.desire2learn.com/d2l/le/calendar/feed/user/feed.ics?token=a4dbdlncxwlroanq2d843"

# Fetch the ICS file
response = requests.get(ics_url)
if response.status_code == 200:
    calendar = icalendar.Calendar.from_ical(response.text)
    # Loop through events
    for event in calendar.walk("VEVENT"):
        summary = event.get("SUMMARY")
        start = event.get("DTSTART").dt  # Can be datetime or date object
        end = event.get("DTEND").dt
        location = event.get("LOCATION")

        print(f"Event: {summary}")
        print(f"Start: {start}")
        print(f"End: {end}")
        print(f"Location: {location}")
        print("-" * 30)
else:
    print("Failed to fetch the ICS feed")
