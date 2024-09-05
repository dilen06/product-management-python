from behave import given
from models import Product, db

@given('a product exists')
def step_given_a_product_exists(context):
    product = Product(name="Test Product", category="Electronics", available=True)
    db.session.add(product)
    db.session.commit()
