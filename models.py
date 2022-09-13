from sqlalchemy import Column, Integer, String, Text, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True)
    image_link = Column(Text)
    title = Column(Text)
    date_posted = Column(String(100))
    location = Column(Text)
    number_of_beds = Column(Text)
    description = Column(Text)
    currency = Column(Text, default=None)
    price = Column(DECIMAL, default=None)

    def __repr__(self):
        return f'Apartments: {self.title}'
