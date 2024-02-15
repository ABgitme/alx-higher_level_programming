-- Set the default database context to the specified database name
SELECT TABLE_NAME AS 'Tables_in_hbtn_test_db_0'
FROM information_schema.tables
WHERE TABLE_SCHEMA = DATABASE();
