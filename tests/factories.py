from faker import Faker
fake = Faker()

def create_fake_product():
    return {
        "name": fake.word(),
        "category": fake.word(),
        "availability": fake.boolean(),
        "price": fake.random_number(),
    }
