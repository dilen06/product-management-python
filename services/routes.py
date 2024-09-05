from flask import request, jsonify
from models import Product, db

# Read a single product by ID
def read_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({"error": "Product not found"}), 404

# Create a new product
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], category=data['category'], available=data['available'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# Update a product by ID
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    if product:
        product.name = data.get('name', product.name)
        product.category = data.get('category', product.category)
        product.available = data.get('available', product.available)
        db.session.commit()
        return jsonify(product.to_dict()), 200
    return jsonify({"error": "Product not found"}), 404

# Delete a product by ID
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Product not found"}), 404

# List all products
def list_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# List products by name
def list_by_name(name):
    products = Product.query.filter_by(name=name).all()
    return jsonify([product.to_dict() for product in products]), 200

# List products by category
def list_by_category(category):
    products = Product.query.filter_by(category=category).all()
    return jsonify([product.to_dict() for product in products]), 200

# List products by availability
def list_by_availability(available):
    products = Product.query.filter_by(available=available).all()
    return jsonify([product.to_dict() for product in products]), 200
