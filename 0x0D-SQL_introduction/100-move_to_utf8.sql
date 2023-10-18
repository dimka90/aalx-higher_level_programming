-- a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- converting the database into utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
-- converting a table into utf-8
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- -- converting a column into utf-8
ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

