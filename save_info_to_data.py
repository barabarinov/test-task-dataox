from db import Session
from models import Apartment


def save_info_to_database(apartment: Apartment) -> None:
    with Session() as session:
        session.add(apartment)
        session.commit()
