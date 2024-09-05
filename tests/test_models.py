import pytest
from models import Product

# Sample test data
def create_sample_product():
    return Product(name="Test Product", category="Electronics", available=True)

# Test for reading a product
def test_read_product(session):
    # Arrange
    product = create_sample_product()
    session.add(product)
    session.commit()

    # Act
    found_product = session.query(Product).filter_by(name="Test Product").first()

    # Assert
    assert found_product is not None
    assert found_product.name == "Test Product"

# Test for updating a product
def test_update_product(session):
    # Arrange
    product = create_sample_product()
    session.add(product)
    session.commit()

    # Act
    product_to_update = session.query(Product).filter_by(name="Test Product").first()
    product_to_update.name = "Updated Product"
    session.commit()

    # Assert
    updated_product = session.query(Product).filter_by(name="Updated Product").first()
    assert updated_product is not None
    assert updated_product.name == "Updated Product"

# Test for deleting a product
def test_delete_product(session):
    # Arrange
    product = create_sample_product()
    session.add(product)
    session.commit()

    # Act
    product_to_delete = session.query(Product).filter_by(name="Test Product").first()
    session.delete(product_to_delete)
    session.commit()

    # Assert
    deleted_product = session.query(Product).filter_by(name="Test Product").first()
    assert deleted_product is None

# Test for listing all products
def test_list_all_products(session):
    # Arrange
    product1 = Product(name="Product 1", category="Electronics", available=True)
    product2 = Product(name="Product 2", category="Books", available=False)
    session.add_all([product1, product2])
    session.commit()

    # Act
    products = session.query(Product).all()

    # Assert
    assert len(products) == 2

# Test for finding a product by name
def test_find_by_name(session):
    # Arrange
    product = create_sample_product()
    session.add(product)
    session.commit()

    # Act
    found_product = session.query(Product).filter_by(name="Test Product").first()

    # Assert
    assert found_product is not None
    assert found_product.name == "Test Product"

# Test for finding a product by category
def test_find_by_category(session):
    # Arrange
    product1 = Product(name="Product 1", category="Electronics", available=True)
    product2 = Product(name="Product 2", category="Books", available=False)
    session.add_all([product1, product2])
    session.commit()

    # Act
    electronics_products = session.query(Product).filter_by(category="Electronics").all()

    # Assert
    assert len(electronics_products) == 1
    assert electronics_products[0].category == "Electronics"

# Test for finding products by availability
def test_find_by_availability(session):
    # Arrange
    product1 = Product(name="Product 1", category="Electronics", available=True)
    product2 = Product(name="Product 2", category="Books", available=False)
    session.add_all([product1, product2])
    session.commit()

    # Act
    available_products = session.query(Product).filter_by(available=True).all()

    # Assert
    assert len(available_products) == 1
    assert available_products[0].available is True
