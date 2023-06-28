from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, Employe

# Add Login
@app_routes.route('/login', methods=['POST'])
def add_login():
    try:
        data = request.get_json()
        login_id = data.get('login_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        login_type = data.get('login_type')
        password = data.get('password')
        belong_to = data.get('belong_to')        

        if not login_id or not first_name or not last_name or not login_type or not password or not belong_to:
            return jsonify({'error': 'Missing required fields.'}), 400

        login = Employe(login_id=login_id, first_name=first_name, last_name=last_name, login_type=login_type, password=password, belong_to=belong_to)
        db.session.add(login)
        db.session.commit()

        return jsonify({'message': 'Employe added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Remove Login by login_id
@app_routes.route('/login/<string:login_id>', methods=['DELETE'])
def remove_login(login_id):
    try:
        login = Employe.query.get(login_id)

        if not login:
            return jsonify({'error': 'Login not found.'}), 404

        db.session.delete(login)
        db.session.commit()

        return jsonify({'message': 'Employe removed successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve all logins
@app_routes.route('/login', methods=['GET'])
def get_logins():
    try:
        logins = Employe.query.all()
        login_list = []
        
        for login in logins:
            login_data = {
                'login_id': login.login_id,
                'first_name': login.first_name,
                'last_name': login.last_name,
                'login_type': login.login_type,
                'password': login.password,
                'belong_to': login.belong_to
            }
            login_list.append(login_data)

        return jsonify(login_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve a login by login_id
@app_routes.route('/login/<string:login_id>', methods=['GET'])
def get_login(login_id):
    try:
        login = Employe.query.get(login_id)

        if not login:
            return jsonify({'error': 'Login not found.'}), 404

        login_data = {
            'login_id': login.login_id,
            'first_name': login.first_name,
            'last_name': login.last_name,
            'login_type': login.login_type,
            'password': login.password,
            'belong_to': login.belong_to
        }

        return jsonify(login_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
