#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie
import ipdb

# Set up database engine and session
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ensure tables are created
Base.metadata.create_all(engine)

# Load data
dev1 = session.query(Dev).filter_by(name="Alice").first()
dev2 = session.query(Dev).filter_by(name="Bob").first()
google = session.query(Company).filter_by(name="Google").first()
freebie1 = session.query(Freebie).filter_by(item_name="T-shirt").first()

# Start debugging session
ipdb.set_trace()
