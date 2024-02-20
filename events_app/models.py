"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    # Add a relationship to the Event model
    events = db.relationship("Event", secondary="guest_event_table", back_populates="guests")

class EventType(enum.Enum):
    ALL = "All"
    PARTY = "Party"
    STUDY = "Study"
    NETWORKING = "Networking"
    OTHER = "Other"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
   
    # Add an event_type column to the Event model
    event_type = db.Column(db.Enum(EventType), default=EventType.ALL)
    # Add a relationship to the Guest model
    guests = db.relationship("Guest", secondary="guest_event_table", back_populates="events")

guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'))
)
