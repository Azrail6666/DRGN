
from .default import DefaultInterface
from sqlalchemy.orm import Session
from database.models import DrgnGameModel

class DrgnGameInterface(DefaultInterface):
    def get_data_by_page(self, page, count):
        with Session(self.connection) as session:
            models = session.query(DrgnGameModel).offset(page * count).limit(count).all()
            return models

    def get_count_models(self, ):
        with Session(self.connection) as session:
            count = session.query(DrgnGameModel).count()
        return count
        