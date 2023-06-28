from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, Transaction, Account

# Add Transaction
@app_routes.route('/transaction', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        tran_id = data.get('tran_id')
        tran_type = data.get('tran_type')
        amount = data.get('amount')
        account_number = data.get('account_number')
        receiver_acc_no = data.get('receiver_acc_no')
        via = data.get('via')

        if not tran_id or not tran_type or not amount or not account_number or not receiver_acc_no or not via:
            return jsonify({'error': 'Missing required fields.'}), 400

        account = Account.query.get(account_number)
        receiver_account = Account.query.get(receiver_acc_no)

        if not account:
            return jsonify({'error': 'Account not found.'}), 404

        if tran_type == 'debit':
            if account.balance < amount:
                return jsonify({'error': 'Insufficient balance.'}), 400
            account.balance -= amount
            receiver_account.balance += amount
        elif tran_type == 'credit':
            account.balance += amount
            receiver_account.balance -= amount
        else:
            return jsonify({'error': 'Invalid transaction type.'}), 400

        transaction = Transaction(tran_id=tran_id, tran_type=tran_type, amount=amount, account_number=account_number, receiver_acc_no=receiver_acc_no, via=via)
        db.session.add(transaction)
        db.session.commit()

        return jsonify({'message': 'Transaction added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Remove Transaction by tran_id
@app_routes.route('/transaction/<string:tran_id>', methods=['DELETE'])
def remove_transaction(tran_id):
    try:
        transaction = Transaction.query.get(tran_id)

        if not transaction:
            return jsonify({'error': 'Transaction not found.'}), 404

        db.session.delete(transaction)
        db.session.commit()

        return jsonify({'message': 'Transaction removed successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve all transactions
@app_routes.route('/transaction', methods=['GET'])
def get_transactions():
    try:
        transactions = Transaction.query.all()
        transaction_list = []

        for transaction in transactions:
            transaction_data = {
                'tran_id': transaction.tran_id,
                'tran_type': transaction.tran_type,
                'date': transaction.date,
                'amount': transaction.amount,
                'account_number': transaction.account_number,
                'receiver_acc_no': transaction.receiver_acc_no
            }
            transaction_list.append(transaction_data)

        return jsonify(transaction_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
