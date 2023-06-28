-- Prepares a MySQL server for the project.
DROP DATABASE IF EXISTS bank_api_db;
CREATE DATABASE IF NOT EXISTS bank_api_db;
CREATE USER IF NOT EXISTS 'bank_api'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON bank_api_db . * TO 'bank_api'@'%';
GRANT SELECT ON performance_schema . * TO 'bank_api'@'%';
