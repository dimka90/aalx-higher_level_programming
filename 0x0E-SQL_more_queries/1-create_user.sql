-- a script that creates the MySQL server user user_0d_1
-- Creating a new user if the user does not exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Granting all the privileges to the usaully created user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- -- Reload the privileges to apply the changes
FLUSH PRIVILEGES;
