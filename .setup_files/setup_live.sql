DROP USER IF EXISTS 'vw_user'@'localhost';
CREATE USER IF NOT EXISTS
              'vw_user'@'localhost'
              IDENTIFIED BY 'vwUser#92';
CREATE DATABASE IF NOT EXISTS votewave_db;
GRANT ALL PRIVILEGES ON votewave_db.* TO 'vw_user'@'localhost';
FLUSH PRIVILEGES;

