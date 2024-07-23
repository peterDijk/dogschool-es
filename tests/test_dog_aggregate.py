import pytest

from unittest import TestCase

from dogschool_es.domainmodel import Dog

class TestDog(TestCase):
    def test_dog(self) -> None:
        dog = Dog("Fido")
        dog.add_trick("roll over")
        
        assert dog.name == "Fido"
        assert dog.tricks == ["roll over"]
        
        events = dog.collect_events()
        assert len(events) == 2