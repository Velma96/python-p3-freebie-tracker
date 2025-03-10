from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    freebies = relationship('Freebie', back_populates='company', overlaps="devs,companies")
    devs = relationship('Dev', secondary='freebies', back_populates='companies', overlaps="freebies")

    def give_freebie(self, dev, item_name, value):
        """Creates a new Freebie associated with this Company and the given Dev"""
        freebie = Freebie(item_name=item_name, value=value, company=self, dev=dev)
        return freebie

    @classmethod
    def oldest_company(cls, session):
        """Returns the company with the earliest founding year"""
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship('Freebie', back_populates='dev', overlaps="companies,freebies")
    companies = relationship('Company', secondary='freebies', back_populates='devs', overlaps="freebies")

    def received_one(self, item_name):
        """Returns True if the dev has received a freebie with the given item_name"""
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, other_dev, freebie):
        """Transfers the freebie to another dev if the current dev owns it"""
        if freebie in self.freebies:
            freebie.dev = other_dev

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

    company = relationship('Company', back_populates='freebies', overlaps="devs,companies")
    dev = relationship('Dev', back_populates='freebies', overlaps="companies,devs")

    def print_details(self):
        """Returns a string with details about the freebie"""
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
