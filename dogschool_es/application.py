
from __future__ import annotations
from uuid import UUID
from typing import Any, Dict

from eventsourcing.application import Application

from dogschool_es.aggregates.dog_aggregate import Dog



class DogSchool(Application):
    is_snapshotting_enabled = True

    def register_dog(self, name: str) -> UUID:
        dog = Dog(name)
        self.save(dog)
        return dog.id

    def add_trick(self, dog_id: UUID, trick: str) -> None:
        dog: Dog = self.repository.get(dog_id)
        dog.add_trick(trick)
        self.save(dog)

    def get_dog(self, dog_id: UUID) -> Dict[str, Any]:
        dog: Dog = self.repository.get(dog_id)
        return {"name": dog.name, "tricks": tuple(dog.tricks)}
