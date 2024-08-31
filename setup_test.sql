DROP USER IF EXISTS 'vw_test_user'@'localhost';
CREATE USER IF NOT EXISTS
              'vw_test_user'@'localhost'
              IDENTIFIED BY 'vw_test_user#92';
CREATE DATABASE IF NOT EXISTS votewave_test_db;
GRANT ALL PRIVILEGES ON votewave_test_db.* TO 'vw_test_user'@'localhost';
FLUSH PRIVILEGES;

