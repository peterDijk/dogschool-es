from eventsourcing.system import System

from dogschool_es.application import DogSchool
from dogschool_es.counter_processapp import Counters
from dogschool_es.tricks_processapp import Tricks

dog_system = System(pipes=[
    [DogSchool, Counters],
    # [DogSchool, Tricks]
    ])