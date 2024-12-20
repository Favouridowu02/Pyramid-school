-- This script is used to set up the database for development
CREATE DATABASE IF NOT EXISTS pyramid_dev_db;
CREATE USER IF NOT EXISTS 'pyramid_dev'@'localhost' IDENTIFIED BY 'pyramid_dev_pwd';
GRANT ALL PRIVILEGES ON `pyramid_dev_db`.* TO 'pyramid_dev'@'localhost';
FLUSH PRIVILEGES;