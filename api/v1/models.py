#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

db = SQLAlchemy()

# It creates a unique id for each row in the database.
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(120), unique=True, default=lambda: str(uuid.uuid4()))

    def serialize(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'


class MainBank(BaseModel):
    branch_id = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))

    def serialize(self) -> dict:
        data = super().serialize()
        data.pop('id')  # Remove the 'id' field from the serialized output
        return data


class Loan(BaseModel):
    loan_id = db.Column(db.String(120), primary_key=True)
    loan_type = db.Column(db.String(120))
    amount = db.Column(db.Float)
    hold_by = db.Column(db.String(120), db.ForeignKey('customer.cust_id'))

    def serialize(self) -> dict:
        return super().serialize()


class Account(BaseModel):
    account_number = db.Column(db.String(120), primary_key=True)
    balance = db.Column(db.Float)
    account_type = db.Column(db.String(120))
    cust_id = db.Column(db.String(120), db.ForeignKey('customer.cust_id'))
    belong_to = db.Column(db.String(120), db.ForeignKey('main_bank.branch_id'))


    def serialize(self) -> dict:
        return super().serialize()

class Customer(BaseModel):
    cust_id = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    nationality = db.Column(db.String(120))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    dob = db.Column(db.String(120))

    def serialize(self) -> dict:
        return super().serialize()

class Transaction(BaseModel):
    tran_id = db.Column(db.String(120), primary_key=True)
    tran_type = db.Column(db.String(120))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float)
    account_number = db.Column(db.String(120), db.ForeignKey('account.account_number'))
    receiver_acc_no = db.Column(db.String(120), db.ForeignKey('account.account_number'))
    via = db.Column(db.String(120), db.ForeignKey('employe.login_id'))

    def serialize(self) -> dict:
        return super().serialize()


class Employe(BaseModel):
    login_id = db.Column(db.String(120), primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    login_type = db.Column(db.String(120))
    password = db.Column(db.String(120))
    belong_to = db.Column(db.String(120), db.ForeignKey('main_bank.branch_id'))

    def serialize(self) -> dict:
        return super().serialize()
