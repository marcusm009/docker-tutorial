from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import requests
from flask_swagger_ui import get_swaggerui_blueprint
import json

def transform_mongo_data(data):
    data['_id'] = str(data['_id'])
    return data

# Swagger UI setup
SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI
API_URL = '/static/swagger.yml'  # Our Swagger schema file

app = Flask(__name__)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Flask App Swagger",
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.config["MONGO_URI"] = "mongodb://mongo-db:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    mongo.db.users.insert_one(data)
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    users_transformed = [transform_mongo_data(user) for user in users]

    # Make a GET request to the ASP.NET Core app
    response = requests.get('http://aspnet-app/weatherforecast')
    message = json.loads(response.text)

    return jsonify({'users': users_transformed, 'forecast': message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)