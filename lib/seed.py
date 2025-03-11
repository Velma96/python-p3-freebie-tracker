#!/usr/bin/env python3

from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Add companies
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Microsoft", founding_year=1975)
company3 = Company(name="Apple", founding_year=1976)
company4 = Company(name="Amazon", founding_year=1994)

# Add developers
dev1 = Dev(name="Alice Johnson")
dev2 = Dev(name="Bob Smith")
dev3 = Dev(name="Charlie Davis")
dev4 = Dev(name="Dana Lee")

# Add freebies
freebie1 = Freebie(item_name="T-shirt", value=20, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Sticker Pack", value=5, company=company2, dev=dev2)
freebie3 = Freebie(item_name="Notebook", value=10, company=company3, dev=dev3)
freebie4 = Freebie(item_name="Mug", value=15, company=company4, dev=dev4)
freebie5 = Freebie(item_name="Pen", value=3, company=company1, dev=dev2)
freebie6 = Freebie(item_name="Hoodie", value=50, company=company2, dev=dev3)
freebie7 = Freebie(item_name="Backpack", value=60, company=company3, dev=dev4)
freebie8 = Freebie(item_name="USB Drive", value=25, company=company4, dev=dev1)

# Add all to session and commit
session.add_all([company1, company2, company3, company4, dev1, dev2, dev3, dev4, 
                 freebie1, freebie2, freebie3, freebie4, freebie5, freebie6, freebie7, freebie8])

session.commit()

print("Database seeded successfully!")

