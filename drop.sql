USE bank_api_db;
-- Drop the Login table
DROP TABLE Login;

-- Drop a foreign key constraint from the Transaction table
ALTER TABLE Transaction
DROP FOREIGN KEY FK_Transaction_Receiver_Account;
