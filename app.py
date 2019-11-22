"""Online Marketplace API"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    price = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name

    def serialize(self):
       """Return product data in easily serializable format"""
       return {
           'id' : self.id,
           'name': self.name,
           'price': self.price
       }


# CRUD methods implemented

# Read All
@app.route('/v1/products', methods=['GET'])
def index():

    products = Product.query.order_by(Product.name).all()
    return jsonify([item.serialize() for item in products])

# Create
@app.route('/v1/product/<int:new_id>', methods=['POST'])
def create(new_id):

    new_name = request.json['name']
    new_price = request.json['price']
    product = Product(id=new_id, name=new_name, price=new_price)

    db.session.add(product)

    try:
        db.session.commit()
        return 'Added product successfully'
    except:
        return 'There was some issue adding this product', 422

# Read One
@app.route('/v1/product/<int:id>', methods=['GET'])
def retrieve(id):

    product = Product.query.get_or_404(id)
    return jsonify(product.serialize())

# Update
@app.route('/v1/product/<int:id>', methods=['PUT'])
def update(id):
    product = Product.query.get_or_404(id)

    if 'name' in request.json:
        product.name = request.json['name']
    elif 'price' in request.json:
        product.price = request.json['price']
    else:
        return 'There is something wrong in the request body', 422

    try:
        db.session.commit()
        return 'Updated product successfully'
    except:
        return 'There was some issue updating this product', 422

# Delete
@app.route('/v1/product/<int:id>', methods=['DELETE'])
def delete(id):
    product_to_delete = Product.query.get_or_404(id)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return 'Deleted product successfully'
    except:
        return 'There was some problem deleting this product', 422


if __name__ == "__main__":

    app.run(debug=True)
