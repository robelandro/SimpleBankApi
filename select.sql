USE bank_api_db;
-- Select all rows from the Branch table
SELECT * FROM Branch;

-- Select specific columns from the Loan table
SELECT Loan_Id, Amount FROM Loan;

-- Select data from multiple tables using JOIN
SELECT c.First_Name, a.Account_No
FROM Customer c
JOIN Customer_Account ca ON c.Cust_Id = ca.Cust_Id
JOIN Account a ON ca.Account_No = a.Account_No;
