from flask import jsonify, request
from api.v1.routes import app_routes
from api.v1.models import db, Customer

# Add Customer
@app_routes.route('/customer', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        cust_id = data.get('cust_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        nationality = data.get('nationality')
        address = data.get('address')
        phone = data.get('phone')
        dob = data.get('dob')

        if not cust_id or not nationality or not first_name or not last_name or not address or not phone or not dob:
            return jsonify({'error': 'Missing required fields.'}), 400

        customer = Customer(cust_id=cust_id, first_name=first_name, last_name=last_name, nationality=nationality, address=address, phone=phone, dob=dob)
        db.session.add(customer)
        db.session.commit()

        return jsonify({'message': 'Customer added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add customer: ' + str(e)}), 500

# Remove Customer by cust_id
@app_routes.route('/customer/<string:cust_id>', methods=['DELETE'])
def remove_customer(cust_id):
    try:
        customer = Customer.query.get(cust_id)

        if not customer:
            return jsonify({'error': 'Customer not found.'}), 404

        db.session.delete(customer)
        db.session.commit()

        return jsonify({'message': 'Customer removed successfully.'})
    except Exception as e:
        return jsonify({'error': 'Failed to remove customer: ' + str(e)}), 500

# Retrieve all customers
@app_routes.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        customer_list = []

        for customer in customers:
            customer_data = {
                'cust_id': customer.cust_id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'nationality': customer.nationality,
                'address': customer.address,
                'phone': customer.phone,
                'dob': customer.dob
            }
            customer_list.append(customer_data)

        return jsonify(customer_list), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve customers: ' + str(e)}), 500
