#!/usr/bin/env python3

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

fake = Faker()

# Create the engine and bind the Base to it
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Seed data using Faker
for _ in range(10):
    company = Company(
        name=fake.company(),
        founding_year=fake.year(),
    )
    session.add(company)

dev1 = Dev(name='Chris')
dev2 = Dev(name='Korir')

freebie1 = Freebie(item_name='Laptop', value=1000, dev=dev1, company=company)
freebie2 = Freebie(item_name='Headphones', value=200, dev=dev2, company=company)
freebie3 = Freebie(item_name='Mouse', value=50, dev=dev1, company=company)

# Add objects to the session and commit to the database
session.add_all([dev1, dev2, freebie1, freebie2, freebie3])

import ipdb; ipdb.set_trace()
session.commit()

session.close()
