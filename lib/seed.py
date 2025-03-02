#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

# Create companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create developers
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Create freebies
freebie1 = Freebie(item_name="T-shirt", value=10, company=google, dev=dev1)
freebie2 = Freebie(item_name="Mug", value=15, company=microsoft, dev=dev2)

# Commit to the database
session.add_all([google, microsoft, dev1, dev2, freebie1, freebie2])
session.commit()

print("Database seeded successfully!")
