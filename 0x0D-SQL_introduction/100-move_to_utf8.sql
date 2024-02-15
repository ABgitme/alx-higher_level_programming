-- Set the character set and collation for the hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- Switch to using the hbtn_0c_0 database
USE hbtn_0c_0;
-- Convert the character set and collation of the first_table to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
