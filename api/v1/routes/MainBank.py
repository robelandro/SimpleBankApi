from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, MainBank

@app_routes.route('/main_bank', methods=['POST'])
def add_main_bank():
    try:
        data = request.get_json()
        branch_id = data.get('branch_id')
        name = data.get('name')
        address = data.get('address')
        phone = data.get('phone')

        if not branch_id or not name or not address or not phone:
            return jsonify({'error': 'Missing required fields.'}), 400

        main_bank = MainBank(branch_id=branch_id, name=name, address=address, phone=phone)
        db.session.add(main_bank)
        db.session.commit()

        return jsonify({'message': 'MainBank added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_routes.route('/main_bank/<string:branch_id>', methods=['DELETE'])
def remove_main_bank(branch_id):
    try:
        main_bank = MainBank.query.get(branch_id)

        if not main_bank:
            return jsonify({'error': 'MainBank not found.'}), 404

        db.session.delete(main_bank)
        db.session.commit()

        return jsonify({'message': 'MainBank removed successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_routes.route('/main_bank/<string:branch_id>', methods=['PUT'])
def update_main_bank(branch_id):
    try:
        main_bank = MainBank.query.get(branch_id)

        if not main_bank:
            return jsonify({'error': 'MainBank not found.'}), 404

        data = request.get_json()
        name = data.get('name')
        address = data.get('address')
        phone = data.get('phone')

        if not name or not address or not phone:
            return jsonify({'error': 'Missing required fields.'}), 400

        main_bank.name = name
        main_bank.address = address
        main_bank.phone = phone
        db.session.commit()

        return jsonify({'message': 'MainBank updated successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_routes.route('/main_bank/<string:branch_id>', methods=['GET'])
def get_main_bank(branch_id):
    try:
        main_bank = MainBank.query.get(branch_id)

        if not main_bank:
            return jsonify({'error': 'MainBank not found.'}), 404

        return jsonify(main_bank.serialize())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_routes.route('/main_bank', methods=['GET'])
def get_all_main_banks():
    try:
        main_banks = MainBank.query.all()
        return jsonify([main_bank.serialize() for main_bank in main_banks])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
