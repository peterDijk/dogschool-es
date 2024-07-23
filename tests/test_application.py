from __future__ import annotations
import os

from uuid import UUID

from unittest import TestCase

from dogschool_es.application import DogSchool


class TestDogSchool(TestCase):
    def test_dog_school(self) -> None:
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool_es.sqlite"
        
        # # Construct application object.
        # school = DogSchool()

        # # Evolve application state.
        # fido_id = school.register_dog("Fido")
        # school.add_trick(fido_id, "roll over")
        # school.add_trick(fido_id, "play dead")

        # # Query application state.
        # dog = school.get_dog(fido_id)
        # assert dog["name"] == "Fido"
        # assert dog["tricks"] == ("roll over", "play dead")
        
        # # Evolve application state.
        # buster_id = school.register_dog("Buster")
        # school.add_trick(buster_id, "roll over")
        # school.add_trick(buster_id, "play dead")

        # # Query application state.
        # dog = school.get_dog(buster_id)
        # assert dog["name"] == "Buster"
        # assert dog["tricks"] == ("roll over", "play dead")      
        
        # del school
        
        school = DogSchool()
        
        fido_id = UUID("0ceec2bcbfe34e3ab5881f5b5ee89e4d")
        fido_details = school.get_dog(fido_id)
        self.assertEqual(fido_details["name"], "Fido")
