#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()


apple = Company(name="Apple", founding_year=1976)
amazon = Company(name="Amazon", founding_year=1994)


dev1 = Dev(name="Charlie")
dev2 = Dev(name="Diana")

# Create  freebies
freebie1 = Freebie(item_name="Sticker Pack", value=5, company=apple, dev=dev1)
freebie2 = Freebie(item_name="Water Bottle", value=20, company=amazon, dev=dev2)


session.add_all([apple, amazon, dev1, dev2, freebie1, freebie2])
session.commit()

print("Database seeded successfully!")
