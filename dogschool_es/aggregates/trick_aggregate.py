from uuid import NAMESPACE_URL, uuid5
from typing import Dict, List

from eventsourcing.domain import Aggregate, event

from dogschool_es.aggregates.dog_aggregate import Dog


class Trick(Aggregate):
    class TrickCreated(Aggregate.Created):
        name: str
    
    class DogAdded(Aggregate.Event):
        dog: Dog
        
    @event(TrickCreated)
    def __init__(self, name) -> None:
        self.name = name
        self.dogs: List[Dog] = []
        
    @classmethod
    def create_id(cls, name):
        return uuid5(NAMESPACE_URL, f'/tricks/{name}/')
    
    @event(DogAdded)
    def add_dog(self, dog: Dog):
        self.dogs.append(dog)