from eventsourcing.application import AggregateNotFound
from eventsourcing.system import ProcessApplication
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.domain import Aggregate, event

from dogschool_es.aggregates.trick_aggregate import Trick
from dogschool_es.database.connection import DatabaseConnection, DatabaseSession
from dogschool_es.helpers.aggregate_to_model import trick_aggregate_to_model
from dogschool_es.read_models.tricks_read_model import TricksWithDogs
from dogschool_es.read_repositories.readrepository import SchoolTricksRepository


db_connection = DatabaseConnection()
engine = db_connection.engine()
session = DatabaseSession(engine).__enter__()
# check closing connection etc
# with statement somewhere higher up
projection_repository = SchoolTricksRepository(session)
TricksWithDogs.metadata.create_all(engine)

class TricksReadModel(ProcessApplication):
    _events_processed = 0
    
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    @policy.register(Trick.DogAdded)
    def _(self, domain_event, process_event):
        trick_id = domain_event.originator_id
        print(f"Trick id: {trick_id}")

        trick = self.repository.get(trick_id)
        print(f"Trick dognames: {trick.dog_names}")
        print(f"Trick version: {trick.version}")
        trick_model = trick_aggregate_to_model(trick)

        try:
            projection_repository.add_trick(trick_model)
            self._events_processed += 1
        except:
            raise Exception("Error adding trick to read model")
        
    @property    
    def amount_events_processed(self):
        return self._events_processed