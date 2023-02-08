"""
        events.py: This file will handle routing operations such as creating, updating,
        and deleting events.
"""
from fastapi import APIRouter, HTTPException, status, Body, Depends, Request
from models.events import Event, EventUpdate
from typing import List
from database.connection import get_session
from sqlmodel import select



event_router = APIRouter(tags=['Events'])



# In app database
events = []


# Get all Events
@event_router.get('/', response_model=List[Event])
async def retrieve_all_event(session=Depends(get_session)) -> List[Event]:
        events = session.exec(select(Event)).all()
        return events



# Get a single event
@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
        event = session.get(Event, id)
        if event:
                return event
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                DETAIL='Event with supplied ID does not exist'
        )

        
        
# Create an event
@event_router.post('/new')
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
        session.add(new_event)
        session.commit()
        session.refresh(new_event)
        return {
                'message': 'Event created successfully'
        }
        


# Update an (existing) event
@event_router.put('/edit/{id}', response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
        event = session.get(Event, id)
        
        if event:
                event_data = new_data.dict(exclude_unset=True)
                for key, value in event_data.items():
                        setattr(event, key, value)
                
                session.add(event)
                session.commit()
                session.refresh(event)
                
                return event
        
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail='Event with supplied ID does not exist'
        )
     
     
        
        



# Delete an Event
@event_router.delete('/delete/{id}')
async def delete_event(id: int, session=Depends(get_session)) -> dict:
        event = session.get(Event, id)
        
        if event:
                session.delete(event)
                
                return {'message': 'Event deleted successfully'}
                
        
        raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = 'Event with supplied ID does not exist'
        )        



# Delete all events
async def delete_all_events() -> dict:
        return {'message': 'Events deleted successfully'}



                 