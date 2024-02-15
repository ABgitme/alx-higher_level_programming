-- List all records of the second_table with a non-null name value
SELECT score, name
-- Specify the table and database
FROM second_table
-- Filter out rows with a null name value
WHERE name IS NOT NULL
-- Order the results by score in descending order
ORDER BY score DESC;
