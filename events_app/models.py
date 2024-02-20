"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    events_attending = db.relationship('Event', secondary='guest_event_table', backref='guests')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)

    guests = db.relationship('Guest', secondary='guest_event_table', backref='events')

    # Stretch challenge
    event_type = db.Column(db.Enum('Party', 'Study', 'Networking', name='event_types'))

guest_event_table = db.Table('guest_event_table',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id')),
    db.Column('guest_id', db.Integer, db.ForeignKey('guests.id'))
)
