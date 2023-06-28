USE bank_api_db;
-- Update the balance of an account in the Account table
UPDATE Account
SET Balance = 6000.00
WHERE Account_No = '300763131';

-- Update the address of a customer in the Customer table
UPDATE Customer
SET Address = 'New Address'
WHERE Cust_Id = '1';
