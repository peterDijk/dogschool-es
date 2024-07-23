from eventsourcing.system import System

from dogschool_es.application import DogSchool
from dogschool_es.processor import Counters

dog_system = System(pipes=[[DogSchool, Counters]])