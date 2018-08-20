from models.customer import Customer
import mlab
from faker import *
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(30):
    print("Saving service", i + 1, "......")
    yob = randint(87,96)
    cust_name = fake.name()
    new_customer = Customer(
        name = cust_name,
        gender = randint(0, 1),
        email = cust_name.replace(' ', '') + str(yob) + "@gmail.com",
        phone = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        contacted = choice([True, False])
    )

    new_customer.save()