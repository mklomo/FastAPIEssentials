"""
    events.py: This file will contain the model definition for events operations.
"""
from pydantic import BaseModel
from typing import List



class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    # Create the config class to show an example: define example event data. This is aimed at guiding
    # us when creating a new event from our API.
    class Config:
        schema_extra = {
                        "example" : {
                            'id': 1,
                            "title": "FastAPI Book Launch",
                            "image": "https:linktomyimage.com/image.png",
                            "description": "We will be discussing \
                            the contents of the FastAPI book in \
                            this event. Ensure to come with your \
                            own copy to win gifts!",
                            "tags": ["python", "fastapi", "book",
                            "launch"],
                            "location": "Google Meet"
                                    }
                        }