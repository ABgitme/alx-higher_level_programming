-- Extract table information from information_schema.tables
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
-- Select specific column attributes for the table
FROM information_schema.columns
-- Filter the columns based on the database name and table name
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
