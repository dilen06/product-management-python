from behave import given, when, then
import requests

# Base URL for API endpoints
BASE_URL = "http://localhost:5000"

@given('a product exists')
def step_given_a_product_exists(context):
    context.product_id = create_sample_product()

@when('I read the product')
def step_when_i_read_the_product(context):
    response = requests.get(f"{BASE_URL}/products/{context.product_id}")
    context.response = response

@then('I should see the product details')
def step_then_i_should_see_the_product_details(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data['name'] == "Test Product"

@when('I update the product with new details')
def step_when_i_update_the_product_with_new_details(context):
    update_data = {"name": "Updated Product"}
    response = requests.put(f"{BASE_URL}/products/{context.product_id}", json=update_data)
    context.response = response

@then('the product should be updated')
def step_then_the_product_should_be_updated(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data['name'] == "Updated Product"

@when('I delete the product')
def step_when_i_delete_the_product(context):
    response = requests.delete(f"{BASE_URL}/products/{context.product_id}")
    context.response = response

@then('the product should be deleted')
def step_then_the_product_should_be_deleted(context):
    assert context.response.status_code == 204

@when('I list all products')
def step_when_i_list_all_products(context):
    response = requests.get(f"{BASE_URL}/products")
    context.response = response

@then('I should see a list of all products')
def step_then_i_should_see_a_list_of_all_products(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert len(data) > 0

@when('I search for the product by name')
def step_when_i_search_for_the_product_by_name(context):
    response = requests.get(f"{BASE_URL}/products?name=Test Product")
    context.response = response

@then('I should see the product details')
def step_then_i_should_see_the_product_details(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data[0]['name'] == "Test Product"

@when('I search for products by category')
def step_when_i_search_for_products_by_category(context):
    response = requests.get(f"{BASE_URL}/products?category=Electronics")
    context.response = response

@then('I should see products in that category')
def step_then_i_should_see_products_in_that_category(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert any(product['category'] == "Electronics" for product in data)

@when('I search for products by availability')
def step_when_i_search_for_products_by_availability(context):
    response = requests.get(f"{BASE_URL}/products?available=true")
    context.response = response

@then('I should see products with that availability status')
def step_then_i_should_see_products_with_that_availability_status(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert all(product['available'] is True for product in data)
