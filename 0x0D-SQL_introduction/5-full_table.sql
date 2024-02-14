-- Select detailed column information about the specified table:
SELECT
    COLUMN_NAME,
    DATA_TYPE,
    COLUMN_KEY,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    EXTRA
-- From the `information_schema.columns` table:
FROM information_schema.columns
-- Filter results based on the current database and the given table name:
WHERE TABLE_SCHEMA = DATABASE()
AND TABLE_NAME = 'first_table';
