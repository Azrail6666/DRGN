import json
from database.interfaces.default import DefaultInterface
from database.models.drgn_game import DrgnGameModel
from sqlalchemy.orm import Session
interface = DefaultInterface()

with open("data.json", 'r') as file:
    games = json.load(file)
with Session(interface.connection) as session:
    for game in games:
        model = DrgnGameModel(
            win_type=game['win_type']
        )
        session.add(model)
    session.commit()
