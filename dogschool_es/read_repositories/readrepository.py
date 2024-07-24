from sqlalchemy.orm import Session

class SchoolTricksRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_tricks(self):
        return self.session.get_tricks()
    
    def add_trick(self, trick):
        # 
        self.session.add(trick)
        self.session.commit()
        
    # def update_trick(self, trick):
    #     self.session.update(trick)
    #     self.session.commit()