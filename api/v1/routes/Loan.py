from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, Loan

# Add Loan
@app_routes.route('/loan', methods=['POST'])
def add_loan():
    try:
        data = request.get_json()
        loan_id = data.get('loan_id')
        loan_type = data.get('loan_type')
        amount = data.get('amount')
        hold_by = data.get('hold_by')

        if not loan_id or not loan_type or not amount or not hold_by:
            return jsonify({'error': 'Missing required fields.'}), 400

        loan = Loan(loan_id=loan_id, loan_type=loan_type, amount=amount, hold_by=hold_by)
        db.session.add(loan)
        db.session.commit()

        return jsonify({'message': 'Loan added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Remove Loan by loan_id
@app_routes.route('/loan/<string:loan_id>', methods=['DELETE'])
def remove_loan(loan_id):
    try:
        loan = Loan.query.get(loan_id)

        if not loan:
            return jsonify({'error': 'Loan not found.'}), 404

        db.session.delete(loan)
        db.session.commit()

        return jsonify({'message': 'Loan removed successfully.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Retrieve all loans
@app_routes.route('/loan', methods=['GET'])
def get_loans():
    try:
        loans = Loan.query.all()
        loan_list = []

        for loan in loans:
            loan_data = {
                'loan_id': loan.loan_id,
                'loan_type': loan.loan_type,
                'amount': loan.amount,
                'hold_by': loan.hold_by
            }
            loan_list.append(loan_data)

        return jsonify(loan_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
