from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, Account

# Add Account
@app_routes.route('/account', methods=['POST'])
def add_account():
    try:
        data = request.get_json()
        account_number = data.get('account_number')
        balance = data.get('balance')
        account_type = data.get('account_type')
        cust_id = data.get('cust_id')
        belong_to = data.get('belong_to')

        if not account_number or not balance or not account_type or not cust_id or not belong_to:
            return jsonify({'error': 'Missing required fields.'}), 400

        account = Account(account_number=account_number, balance=balance, account_type=account_type, cust_id=cust_id, belong_to=belong_to)
        db.session.add(account)
        db.session.commit()

        return jsonify({'message': 'Account added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Remove Account by account_number
@app_routes.route('/account/<string:account_number>', methods=['DELETE'])
def remove_account(account_number):
    try:
        account = Account.query.get(account_number)

        if not account:
            return jsonify({'error': 'Account not found.'}), 404

        db.session.delete(account)
        db.session.commit()

        return jsonify({'message': 'Account removed successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve all accounts
@app_routes.route('/account', methods=['GET'])
def get_accounts():
    try:
        accounts = Account.query.all()
        account_list = []

        for account in accounts:
            account_data = {
                'account_number': account.account_number,
                'balance': account.balance,
                'account_type': account.account_type,
                'cust_id': account.cust_id
            }
            account_list.append(account_data)

        return jsonify(account_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
