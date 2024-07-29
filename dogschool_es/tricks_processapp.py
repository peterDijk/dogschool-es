import os
from eventsourcing.application import AggregateNotFound
from eventsourcing.system import Application
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.domain import Aggregate, event

from dogschool_es.aggregates.dog_aggregate import Dog
from dogschool_es.aggregates.trick_aggregate import Trick

class Tricks(Application):
    def add_trick(trick_name: str, dog: Dog):
        try:
            trick_id = Trick.create_id(trick_name)
            trick = self.repository.get(trick_id)
        except AggregateNotFound:
            trick = Trick(trick_name)
        trick.add_dog(dog.name)
        self.save(trick)
        
    def get_trick(self, trick_name):
        trick_id = Trick.create_id(trick_name)
        try:
            trick = self.repository.get(trick_id)
        except AggregateNotFound:
            return None
        return trick