from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer())

    
    freebies = relationship("Freebie", back_populates="company", cascade="all, delete-orphan")

    
    devs = relationship("Dev", secondary="freebies", back_populates="companies", overlaps="freebies")

    def __repr__(self):
        return f'<Company {self.name}, Founded {self.founding_year}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    
    freebies = relationship("Freebie", back_populates="dev", cascade="all, delete-orphan")

    
    companies = relationship("Company", secondary="freebies", back_populates="devs", overlaps="freebies")

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

   
    company = relationship("Company", back_populates="freebies", overlaps="devs,companies")
    dev = relationship("Dev", back_populates="freebies", overlaps="devs,companies")

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

    def __repr__(self):
        return f'<Freebie {self.item_name}, Worth {self.value}>'


#1. Get a Developer and Their Freebies, companies
    #dev = session.query(Dev).filter_by(name="Alice Johnson").first()
    #dev.freebies
    #dev.companies
#2. Get a Company and Their Freebies,devs
   # company = session.query(Company).filter_by(name="Google").first()
   # company.freebies
    #company.devs
#3. Get a Freebie and Its Dev & Company
    #freebie = session.query(Freebie).filter_by(item_name="T-shirt").first()
    #freebie.dev  
    #freebie.company