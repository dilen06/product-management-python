import pytest
from app import app  # Assuming the app is created in app.py
from models import Product
import json

# Helper function to create a sample product
def create_sample_product():
    return {"name": "Test Product", "category": "Electronics", "available": True}

# Test for the CREATE route (POST /products)
def test_create_product(client):
    # Arrange
    new_product = create_sample_product()

    # Act
    response = client.post('/products', data=json.dumps(new_product), content_type='application/json')

    # Assert
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Test Product"

# Test for the READ route (GET /products/<id>)
def test_read_product(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act
    response = client.get(f'/products/{product.id}')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == "Test Product"

# Test for the UPDATE route (PUT /products/<id>)
def test_update_product(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()
    
    # Update data
    updated_data = {"name": "Updated Product", "category": "Electronics", "available": True}

    # Act
    response = client.put(f'/products/{product.id}', data=json.dumps(updated_data), content_type='application/json')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == "Updated Product"

# Test for the DELETE route (DELETE /products/<id>)
def test_delete_product(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act
    response = client.delete(f'/products/{product.id}')

    # Assert
    assert response.status_code == 204

# Test for LIST ALL route (GET /products)
def test_list_all_products(client, session):
    # Arrange
    product1 = Product(name="Product 1", category="Electronics", available=True)
    product2 = Product(name="Product 2", category="Books", available=False)
    session.add_all([product1, product2])
    session.commit()

    # Act
    response = client.get('/products')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

# Test for SEARCH by name (GET /products?name=)
def test_search_by_name(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act
    response = client.get('/products?name=Test Product')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]['name'] == "Test Product"

# Test for SEARCH by category (GET /products?category=)
def test_search_by_category(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act
    response = client.get('/products?category=Electronics')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]['category'] == "Electronics"

# Test for SEARCH by availability (GET /products?available=)
def test_search_by_availability(client, session):
    # Arrange
    product = Product(name="Test Product", category="Electronics", available=True)
    session.add(product)
    session.commit()

    # Act
    response = client.get('/products?available=true')

    # Assert
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]['available'] is True
