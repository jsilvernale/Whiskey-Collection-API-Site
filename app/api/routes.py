from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Whiskey, whiskey_schema, whiskies_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/whiskey', methods = ['POST'])
@token_required
def create_entry(current_user_token):
    brand = request.json['brand']
    type = request.json['type']
    alc_percent = request.json['alc_percent']
    user_token = current_user_token.token

    whiskey = Whiskey(brand, type, alc_percent, user_token = user_token)
    
    db.session.add(whiskey)
    db.session.commit()

    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

@api.route('/whiskies', methods = ['GET'])
@token_required
def get_whiskies(current_user_token):
    a_user = current_user_token.token
    whiskies = Whiskey.query.filter_by(user_token = a_user).all()
    response = whiskies_schema.dump(whiskies)
    return jsonify(response)

@api.route('/whiskey/<whiskey_id>', methods = ['GET'])
@token_required
def get_single_whiskey(current_user_token, whiskey_id):
    whiskey = Whiskey.query.get(whiskey_id)
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)

@api.route('/whiskies/<whiskey_id>', methods = ['DELETE'])
@token_required
def delete_whiskey(current_user_token, whiskey_id):
    whiskey = Whiskey.query.get(whiskey_id)
    db.session.delete(whiskey)
    db.session.commit()
    response = whiskey_schema.dump(whiskey)
    return jsonify(response)


