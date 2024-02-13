-- Set the default database context to the information_schema database
USE information_schema;
-- Select the schema_name column from the SCHEMATA table
-- The SCHEMATA table contains metadata about all databases on the MySQL server
SELECT schema_name AS "Database"
FROM SCHEMATA;
