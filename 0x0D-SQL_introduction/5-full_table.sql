-- This line selects specific columns from the information_schema.columns table.
SELECT COLUMN_NAME, DATA_TYPE, COLUMN_KEY, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
-- From the information_schema.columns table which contains various data dictionary information.
FROM information_schema.columns
-- Filter results to only include columns belonging to the database passed as an argument.
WHERE TABLE_SCHEMA = DATABASE()
-- Further filter to only include columns from the specified table named 'first_table'.
AND TABLE_NAME = 'first_table';
