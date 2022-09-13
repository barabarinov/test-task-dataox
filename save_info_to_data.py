from db import Session
from models import Apartment


def save_info_to_database(values: list):

    with Session() as session:
        apartment = Apartment(
            image_link=values[0],
            title=values[1],
            date_posted=values[2],
            location=values[3],
            number_of_beds=values[4],
            description=values[5],
            currency=values[6],
            price=values[7],
        )

        session.add(apartment)
        session.commit()
