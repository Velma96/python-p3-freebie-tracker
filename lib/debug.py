#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie
import ipdb

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)


dev1 = session.query(Dev).filter_by(name="Charlie").first()
dev2 = session.query(Dev).filter_by(name="Diana").first()
apple = session.query(Company).filter_by(name="Apple").first()
freebie1 = session.query(Freebie).filter_by(item_name="Sticker Pack").first()

# Start debugging session
ipdb.set_trace()
