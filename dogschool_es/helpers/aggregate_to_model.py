from dogschool_es.aggregates.trick_aggregate import Trick
from dogschool_es.read_models.tricks_read_model import TricksWithDogs

def trick_aggregate_to_model(trick: Trick) -> TricksWithDogs:
    return TricksWithDogs(trick_id=trick.id, trick_name=trick.name, dog_names=trick.dog_names)
