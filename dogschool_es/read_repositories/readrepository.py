from sqlalchemy.orm import Session

from dogschool_es.read_models.tricks_read_model import TricksWithDogs

class SchoolTricksRepository:
    def __init__(self, session: Session):
        self.session = session

    # def get_tricks(self):
    #     return self.session.get_tricks()
    
    def add_trick(self, trick):
        # check existing then update
        try:
            self.session.add(trick)
        except:
            self.session.query(TricksWithDogs).filter(TricksWithDogs.trick_id == trick.trick_id).update({ "dog_names": trick.dog_names })
        self.session.commit()
        
    # def update_trick(self, trick):
    #     self.session.update(trick)
    #     self.session.commit()