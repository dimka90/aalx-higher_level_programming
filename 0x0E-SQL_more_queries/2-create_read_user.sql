-- a script that creates the database hbtn_0d_2 and the user user_0d_2
-- Creating a new database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating a new user if the user  does not exit with  password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Granting privillages the select privillages to the newly created user
GRANT SELECT  ON 'htb_0d_2'.*  TO 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Reload the privillages to apply changes
FLUSH PRIVILLAGES;
