import os
from unittest import TestCase

from eventsourcing.system import SingleThreadedRunner

from dogschool_es.aggregates.trick_aggregate import Trick
from dogschool_es.application import DogSchool
from dogschool_es.tricks_processapp import Tricks
from dogschool_es.system import dog_system
from dogschool_es.tricks_readmodel_processapp import TricksReadModel


class TestSystem(TestCase):
    def test_system(self) -> None:
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool_es_mockDB2dogs3tricks.sqlite"        

        runner = SingleThreadedRunner(dog_system)
        runner.start()
        
        # test projection is empty? integration test
        
        
        # Get the application objects.
        school = runner.get(DogSchool)
        tricks = runner.get(Tricks)
        tricks_readmodel = runner.get(TricksReadModel)
        
        # Enable when rebuild from stored events.
        tricks.pull_and_process(leader_name=DogSchool.__name__, start=1) # start from the beginning!
        tricks_readmodel.pull_and_process(leader_name=Tricks.__name__, start=1) # start from the beginning!
        assert tricks_readmodel.amount_events_processed == 3 # 3x a dog is added to a trick
        
        trick = tricks.get_trick('roll over')
        assert isinstance(trick, Trick)
        assert trick.dog_names == ["Fido", "Buster"]
        
        trick2 = tricks.get_trick('play dead')
        assert trick2.dog_names == ["Fido"]
        
        
        
        # test read model content here, integration test
        

        # Stop the runner.
        runner.stop()