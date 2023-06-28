USE bank_api_db;
-- Add a new column to the Customer table
ALTER TABLE Customer
ADD Email VARCHAR(120);

-- Modify the data type of a column in the Loan table
ALTER TABLE Loan
MODIFY COLUMN Amount DECIMAL(10, 2);

-- Rename a column in the Account table
ALTER TABLE Account
CHANGE COLUMN Account_Type Type VARCHAR(120);
