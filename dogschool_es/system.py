from eventsourcing.system import System

from dogschool_es.application import DogSchool
from dogschool_es.tricks_processapp import Tricks
from dogschool_es.tricks_readmodel_processapp import TricksReadModel

dog_system = System(pipes=[
    [DogSchool, Tricks],
    [Tricks, TricksReadModel],
    ])