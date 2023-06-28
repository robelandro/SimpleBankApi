from flask import Flask, make_response, jsonify
from flask_cors import CORS
from api.v1.routes import app_routes
from api.v1.models import db

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bank_api:@localhost/bank_api_db'
app.register_blueprint(app_routes)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
db.init_app(app)

@app.teardown_appcontext
def close_db(error):
    db.session.close()
    print(f'Closing Databases: {error}') 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '5000'
    with app.app_context():
        db.create_all()
    app.run(host=host, port=port, threaded=True)
