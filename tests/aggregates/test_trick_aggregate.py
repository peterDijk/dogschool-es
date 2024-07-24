from uuid import NAMESPACE_URL, uuid5
from unittest import TestCase

from dogschool_es.aggregates.dog_aggregate import Dog
from dogschool_es.aggregates.trick_aggregate import Trick


class TestTrickCase(TestCase):
    def test_trick(self) -> None:
        
        fido = Dog("Fido")
        buster = Dog("Buster")
        trick = Trick("roll over")
        
        create_id = Trick.create_id("roll over")
        expected_id = uuid5(NAMESPACE_URL, '/tricks/roll over/')
        assert create_id == expected_id
        
        trick.add_dog(fido)
        trick.add_dog(buster)
        events = trick.collect_events()
        assert len(events) == 3
        assert isinstance(events[0], Trick.TrickCreated)
        assert isinstance(events[1], Trick.DogAdded)
        assert isinstance(events[2], Trick.DogAdded)
        
        assert events[0].name == "roll over"
        assert isinstance(events[1].dog, Dog)
        assert trick.dogs == [fido, buster]