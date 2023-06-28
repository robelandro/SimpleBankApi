-- START TRANSACTION
START TRANSACTION;
-- Prepares a MySQL server for the project.
DROP DATABASE IF EXISTS bank_api_db;
CREATE DATABASE IF NOT EXISTS bank_api_db;
CREATE USER IF NOT EXISTS 'bank_api'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON bank_api_db . * TO 'bank_api'@'%';
GRANT SELECT ON performance_schema . * TO 'bank_api'@'%';
USE bank_api_db;
-- CREATE TABLE statements

-- Branch
CREATE TABLE Branch (
  Branch_Id VARCHAR(120) PRIMARY KEY,
  Name VARCHAR(120),
  Address VARCHAR(120)
);

-- Login_Type
CREATE TABLE Login_Type (
  Username VARCHAR(120) PRIMARY KEY,
  Login_Type VARCHAR(120)
);

-- Login
CREATE TABLE Login (
  Login_Id VARCHAR(120) PRIMARY KEY,
  Password VARCHAR(120),
  Username VARCHAR(120),
  Branch_Id VARCHAR(120),
  CONSTRAINT FK_Login_Login_Type FOREIGN KEY (Username) REFERENCES Login_Type(Username),
  CONSTRAINT FK_Login_Branch FOREIGN KEY (Branch_Id) REFERENCES Branch(Branch_Id)
);

-- Loan_Type
CREATE TABLE Loan_Type (
  Loan_Id VARCHAR(120) PRIMARY KEY,
  Loan_Type VARCHAR(120)
);

-- Loan
CREATE TABLE Loan (
  Loan_Id VARCHAR(120) PRIMARY KEY,
  Amount FLOAT,
  Branch_Id VARCHAR(120),
  CONSTRAINT FK_Loan_Branch FOREIGN KEY (Branch_Id) REFERENCES Branch(Branch_Id)
);

-- Account
CREATE TABLE Account (
  Account_No VARCHAR(120) PRIMARY KEY,
  Account_Type VARCHAR(120),
  Balance FLOAT,
  Branch_Id VARCHAR(120),
  CONSTRAINT FK_Account_Branch FOREIGN KEY (Branch_Id) REFERENCES Branch(Branch_Id)
);

-- Transaction
CREATE TABLE Transaction (
  Tran_Id VARCHAR(120) PRIMARY KEY,
  Tran_Type VARCHAR(120),
  Receiver_Account_No VARCHAR(120),
  Sender_Account_No VARCHAR(120),
  Via VARCHAR(120),
  Amount FLOAT,
  Date DATETIME,
  CONSTRAINT FK_Transaction_Receiver_Account FOREIGN KEY (Receiver_Account_No) REFERENCES Account(Account_No),
  CONSTRAINT FK_Transaction_Sender_Account FOREIGN KEY (Sender_Account_No) REFERENCES Account(Account_No)
);

-- Customer
CREATE TABLE Customer (
  Cust_Id VARCHAR(120) PRIMARY KEY,
  First_Name VARCHAR(120),
  Last_Name VARCHAR(120),
  Address VARCHAR(120),
  Nationality VARCHAR(120),
  Dob VARCHAR(120)
);

-- Phone
CREATE TABLE Phone (
  Phone_Number VARCHAR(120) PRIMARY KEY,
  Cust_Id VARCHAR(120),
  CONSTRAINT FK_Phone_Customer FOREIGN KEY (Cust_Id) REFERENCES Customer(Cust_Id)
);

-- Customer_Account
CREATE TABLE Customer_Account (
  Cust_Id VARCHAR(120),
  Account_No VARCHAR(120),
  PRIMARY KEY (Cust_Id, Account_No),
  CONSTRAINT FK_Customer_Account_Customer FOREIGN KEY (Cust_Id) REFERENCES Customer(Cust_Id),
  CONSTRAINT FK_Customer_Account_Account FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);

-- Customer_Loan
CREATE TABLE Customer_Loan (
  Cust_Id VARCHAR(120),
  Loan_Id VARCHAR(120),
  PRIMARY KEY (Cust_Id, Loan_Id),
  CONSTRAINT FK_Customer_Loan_Customer FOREIGN KEY (Cust_Id) REFERENCES Customer(Cust_Id),
  CONSTRAINT FK_Customer_Loan_Loan FOREIGN KEY (Loan_Id) REFERENCES Loan(Loan_Id)
);

-- INSERT statements

-- Branch
INSERT INTO Branch (Branch_Id, Name, Address)
VALUES ('1', 'Branch 1', 'Addis Ababa'),
       ('2', 'Branch 2', 'Adama');

-- Login_Type
INSERT INTO Login_Type (Username, Login_Type)
VALUES ('robel', 'admin'),
       ('yared', 'user');

-- Login
INSERT INTO Login (Login_Id, Password, Username, Branch_Id)
VALUES ('1', 'password1', 'robel', '1'),
       ('2', 'password2', 'yared', '2');

-- Loan_Type
INSERT INTO Loan_Type (Loan_Id, Loan_Type)
VALUES ('1', 'Long Term'),
       ('2', 'Short Term');

-- Loan
INSERT INTO Loan (Loan_Id, Amount, Branch_Id)
VALUES ('1', 1000.00, '1'),
       ('2', 2000.00, '2');

-- Account
INSERT INTO Account (Account_No, Account_Type, Balance, Branch_Id)
VALUES ('300763131', 'saving', 5000.00, '1'),
       ('300763132', 'normal', 3000.00, '2');

-- Transaction
INSERT INTO Transaction (Tran_Id, Tran_Type, Receiver_Account_No, Sender_Account_No, Via, Amount, Date)
VALUES ('1', 'transfer', '300763131', '300763132', 'Internet', 100.00, '2023-06-8'),
       ('2', 'transfer', '300763132', '300763131', 'office', 200.00, '2023-06-8'),
       ('3', 'deposit', '300763131', '300763131', 'office', 100.00, '2023-06-8'),
       ('4', 'withdraw', '300763132', '300763132', 'office', 200.00, '2023-06-8');

-- Customer
INSERT INTO Customer (Cust_Id, First_Name, Last_Name, Address, Nationality, Dob)
VALUES ('1', 'Able', 'Ademu', 'Addis Ababa', 'Ethiopian', '1990-01-01'),
       ('2', 'Jane', 'Smith', 'Address 2', 'Austrlian', '1995-02-02');

-- Phone
INSERT INTO Phone (Phone_Number, Cust_Id)
VALUES ('1234567890', '1'),
       ('9876543210', '2');

-- Customer_Account
INSERT INTO Customer_Account (Cust_Id, Account_No)
VALUES ('1', '300763131'),
       ('2', '300763132');

-- Customer_Loan
INSERT INTO Customer_Loan (Cust_Id, Loan_Id)
VALUES ('1', '1'),
       ('2', '2');

-- COMMIT the transaction
COMMIT;
