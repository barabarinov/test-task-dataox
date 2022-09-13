from db import engine
from models import Apartment


def create_tables():
    Apartment.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
