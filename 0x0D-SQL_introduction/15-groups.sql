-- List the number of records with the same score in the second_table
SELECT score, COUNT(*) AS number
-- Specify the table and database
FROM second_table
-- Group records by score
GROUP BY score
-- Order the results by the number of records in descending order
ORDER BY number DESC;
