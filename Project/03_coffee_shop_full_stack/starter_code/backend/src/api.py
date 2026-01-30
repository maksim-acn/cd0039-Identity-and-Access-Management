import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
Initialize the database
'''
db_drop_and_create_all()

# ROUTES
@app.route('/drinks', methods=['GET'])
def get_drinks():
    """Public endpoint to get all drinks (short representation)
    """
    try:
        drinks = Drink.query.all()
        drinks_short = [drink.short() for drink in drinks]
        
        return jsonify({
            "success": True,
            "drinks": drinks_short
        }), 200
        
    except Exception as e:
        abort(422)

@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    """Protected endpoint to get all drinks (long representation)
    """
    try:
        drinks = Drink.query.all()
        drinks_long = [drink.long() for drink in drinks]
        
        return jsonify({
            "success": True,
            "drinks": drinks_long
        }), 200
        
    except Exception as e:
        abort(422)

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    """Protected endpoint to create a new drink
    """
    body = request.get_json()
    new_title = body.get('title', None)
    new_recipe = body.get('recipe', None)
    
    if not new_title or not new_recipe:
        abort(400)
        
    try:
        drink = Drink(title=new_title, recipe=json.dumps(new_recipe))
        drink.insert()
        
        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        }), 200
        
    except Exception as e:
        abort(422)

@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, id):
    """Protected endpoint to update a drink
    """
    body = request.get_json()
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    
    if not drink:
        abort(404)
        
    try:
        if 'title' in body:
            drink.title = body['title']
            
        if 'recipe' in body:
            drink.recipe = json.dumps(body['recipe'])
            
        drink.update()
        
        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        }), 200
        
    except Exception as e:
        abort(422)

@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    """Protected endpoint to delete a drink
    """
    drink = Drink.query.filter(Drink.id == id).one_or_none()
    
    if not drink:
        abort(404)
        
    try:
        drink.delete()
        
        return jsonify({
            "success": True,
            "delete": id
        }), 200
        
    except Exception as e:
        abort(422)

# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
