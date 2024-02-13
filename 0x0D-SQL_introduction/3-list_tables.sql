-- Set the default database context to the specified database name
USE mysql;
-- Select the table_name column from the information_schema.tables view
SELECT table_name
-- The information_schema.tables view contains metadata about all tables in the MySQL server
FROM information_schema.tables
-- Filtering is applied to only retrieve tables from the specified database
WHERE table_schema = 'mysql';
