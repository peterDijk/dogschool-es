import os
from eventsourcing.application import AggregateNotFound
from eventsourcing.system import ProcessApplication
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.domain import Aggregate, event

from dogschool_es.aggregates.dog_aggregate import Dog
from dogschool_es.aggregates.trick_aggregate import Trick

class Tricks(ProcessApplication):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""
        
    @policy.register(Dog.TrickAdded)
    def _(self, domain_event, process_event):
        event_trick_name = domain_event.trick
        dog_id = domain_event.originator_id
        # dog = self.
        try:
            trick_id = Trick.create_id(event_trick_name)
            trick = self.repository.get(trick_id)
        except AggregateNotFound:
            trick = Trick(event_trick_name)
        trick.add_dog(dog)
        process_event.collect_events(trick)
            