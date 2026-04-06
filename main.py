# CIS 2131 Project 4 - Event Planning App
# I'm just so sick of snake case...sorry.


# def main():
    # organizer mode
# events = {
# "Python Workshop": {
#     "max_attendees": 30,
#     "attendees": ["Alice", "Bob"]
# }
# }

# create event
def create_event(events, event_name, max_attendees):
    attendee_names : str = None
    if event_name not in events:
        events = { event_name : {"max_attendees" : [None] * max_attendees, 
                                "attendees" : [attendee_names] * max_attendees}}
    else:
        raise ValueError("Event already exists, please enter a new event.")
    return events
# update event
def updateEvent(eventName, maxAttendees):
    pass

# delete event
def deleteEvent(eventName):
    pass

# view roster: print the list of attendees for a specific event
def viewRoster(eventName):
    pass

# attendee mode

# view events
def viewAllEvents():
    pass

# rsvp to an event
def createRsvp():
    pass

# cancel rsvp
def cancelRsvp():
    pass

# view my events
def viewMyEvents():
    pass

# helper methods
def create_events_dict(event_name, max_size, list_of_names):
    events = { event_name : {
        'max_attendees' : max_size,
        'attendee_names' : [list_of_names] * max_size
        }
        }
    return events

if '__name__' == '__main__':
    test_events = {
    "Python Workshop": {
        "max_attendees": 30,
        "attendees": ["Alice", "Bob"]
    }
}
    new_event_test = input("New name for event: ")
    new_attendee_test = int(input("Enter the maximun attendee count: "))
    create_event(test_events, new_event_test, new_attendee_test)
    for event in test_events.items():
        print(test_events[event])
