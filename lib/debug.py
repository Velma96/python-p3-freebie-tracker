#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

# Set up database connection
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    print("\nDebug session started. Use session.query(Model).all() to view data.")
    print("Available Models: Company, Dev, Freebie")
    print("Example Queries:")
    print("   session.query(Company).all()  # View all companies")
    print("   session.query(Dev).all()      # View all developers")
    print("   session.query(Freebie).all()  # View all freebies")
    print("\nTip: Use dev.freebies, company.devs, freebie.print_details(), etc.")

    import ipdb; ipdb.set_trace()
