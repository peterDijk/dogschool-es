import os
import pytest
from unittest import TestCase

from eventsourcing.system import SingleThreadedRunner

from dogschool_es.application import DogSchool
from dogschool_es.counter_processapp import Counters
from dogschool_es.system import dog_system


class TestSystem(TestCase):
    # @pytest.mark.skip(reason="This test is not working")
    def test_system(self) -> None:
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool_es_mockDB2dogs3tricks.sqlite"        

        runner = SingleThreadedRunner(dog_system)
        runner.start()
        
        
        # Get the application objects.
        school = runner.get(DogSchool)
        counters = runner.get(Counters)
        
        # Enable when rebuild from stored events.
        counters.pull_and_process(leader_name=DogSchool.__name__)
        

        # Check the results of processing the events.
        assert counters.get_count('roll over') == 2 # disk-database has 2 roll over trick added events
        assert counters.get_count('fetch ball') == 0
        assert counters.get_count('play dead') == 1

        # Stop the runner.
        runner.stop()