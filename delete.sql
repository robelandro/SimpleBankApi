USE bank_api_db;

-- Delete multiple rows from the Transaction table based on a condition
DELETE FROM Transaction
WHERE Receiver_Account_No = '300763132';
select * from Transaction;
