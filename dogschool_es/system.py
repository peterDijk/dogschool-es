from eventsourcing.system import System

from dogschool_es.application import DogSchool
from dogschool_es.counter_processapp import Counters

dog_system = System(pipes=[
    [DogSchool, Counters],
    ])