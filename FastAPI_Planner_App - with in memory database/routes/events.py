"""
        events.py: This file will handle routing operations such as creating, updating,
        and deleting events.
"""
from fastapi import APIRouter, HTTPException, status, Body
from models.events import Event
from typing import List



event_router = APIRouter(tags=['Events'])



# In app database
events = []


# Get all Events
@event_router.get('/', response_model=List[Event])
async def retrieve_all_event(id: int) -> List[Event]:
        return events



# Get a single event
@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: int) -> Event:
        for event in events:
                if event.id == id:
                        return event
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                DETAIL='Event with supplied ID does not exist'
        )
        
        
# Create an event
@event_router.post('/new')
async def create_event(body:Event = Body(...)) -> dict:
        events.append(body)
        return {
                'message': 'Event created successfully'
        }
        


# Delete an Event
@event_router.delete('/{id}')
async def delete_event(id: int) -> dict:
        for event in events:
                if event.id == id:
                        events.remove(event)
                        return {'message': 'Event deleted successfully'}
                
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = 'Event with supplied ID does not exist'
        )        


# Delete all events
async def delete_all_events() -> dict:
        return {'message': 'Events deleted successfully'}                 