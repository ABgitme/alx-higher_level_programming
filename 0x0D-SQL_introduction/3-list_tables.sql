-- Set the default database context to the specified database name
SELECT TABLE_NAME
FROM information_schema.tables
WHERE TABLE_SCHEMA = DATABASE();
