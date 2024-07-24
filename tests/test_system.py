import os
import pytest
from unittest import TestCase

from eventsourcing.system import SingleThreadedRunner

from dogschool_es.aggregates.trick_aggregate import Trick
from dogschool_es.application import DogSchool
from dogschool_es.tricks_processapp import Tricks
from dogschool_es.system import dog_system


class TestSystem(TestCase):
    def test_system(self) -> None:
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool_es_mockDB2dogs3tricks.sqlite"        

        runner = SingleThreadedRunner(dog_system)
        runner.start()
        
        
        # Get the application objects.
        school = runner.get(DogSchool)
        tricks = runner.get(Tricks)
        
        # Enable when rebuild from stored events.
        tricks.pull_and_process(leader_name=DogSchool.__name__)

        
        trick = tricks.get_trick('roll over')
        assert isinstance(trick, Trick)
        assert trick.dog_names == ["Fido", "Buster"]
        
        trick2 = tricks.get_trick('play dead')
        assert trick2.dog_names == ["Fido"]
        

        # Stop the runner.
        runner.stop()