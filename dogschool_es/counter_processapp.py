from uuid import NAMESPACE_URL, uuid5
import logging

from eventsourcing.application import AggregateNotFound
from eventsourcing.system import ProcessApplication
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.domain import Aggregate, event

from dogschool_es.aggregates.dog_aggregate import Dog

class Counters(ProcessApplication):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Dog.TrickAdded)
    def _(self, domain_event, process_event):
        trick = domain_event.trick
        logging.info(f"Counting trick: {trick}")
        try:
            counter_id = Counter.create_id(trick)
            counter = self.repository.get(counter_id)
        except AggregateNotFound:
            counter = Counter(trick)
        counter.increment()
        process_event.collect_events(counter)

    def get_count(self, trick):
        counter_id = Counter.create_id(trick)
        try:
            counter = self.repository.get(counter_id)
        except AggregateNotFound:
            return 0
        return counter.count


class Counter(Aggregate):
    def __init__(self, name):
        self.name = name
        self.count = 0

    @classmethod
    def create_id(cls, name):
        return uuid5(NAMESPACE_URL, f'/counters/{name}')

    @event('Incremented')
    def increment(self):
        self.count += 1