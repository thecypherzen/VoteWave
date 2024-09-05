DROP USER IF EXISTS 'vw_test_user'@'localhost';
CREATE USER IF NOT EXISTS
              'vw_test_user'@'localhost'
              IDENTIFIED BY 'vwTestUser#92';
DROP DATABASE IF EXISTS votewave_test_db;
CREATE DATABASE votewave_test_db;
GRANT ALL PRIVILEGES ON votewave_test_db.* TO 'vw_test_user'@'localhost';
FLUSH PRIVILEGES;

