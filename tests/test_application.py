from __future__ import annotations
import os

from uuid import UUID

from unittest import TestCase

from dogschool_es.application import DogSchool


class TestDogSchool(TestCase):
    def test_dog_school(self) -> None:
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool_es_mockDB2dogs3tricks.sqlite"
        
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

        # # Query application state.
        # dog = school.get_dog(buster_id)
        # assert dog["name"] == "Buster"
        # assert dog["tricks"] == ("roll over",)      
        
        # del school
        
        # school = DogSchool()
        
        # # with the given sqlite database, the following code pass the test. 
        # # This proves the aggregate is build up from events stored in sqlite database.
        # fido_id = UUID("ae13d396395a43ce8799e0a7b2341dfe")
        # fido_details = school.get_dog(fido_id)
        # self.assertEqual(fido_details["name"], "Fido")
        # self.assertEqual(fido_details["tricks"], ("roll over", "play dead"))

        # buster_id = UUID("84c72235755e4f42a0c57cad76594d99")
        # buster_details = school.get_dog(buster_id)
        # self.assertEqual(buster_details["name"], "Buster")
        # self.assertEqual(buster_details["tricks"], ("roll over",))        