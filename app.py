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


# CRUD methods implemented

# Read All
@app.route('/', methods=['GET'])
def index():
    return

# Create
@app.route('/<int:new_id>', methods=['POST'])
def create(new_id):
    return

# Read One
@app.route('/<int:id>', methods=['GET'])
def retrieve(id):
    return

# Update
@app.route('/<int:id>', methods=['PUT'])
def update(id):
    return

# Delete
@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return
