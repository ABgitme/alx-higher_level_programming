-- Define a variable to store the database name
SET @database = $database;
-- Find the ID of the California state
SELECT id FROM @database.states WHERE name = 'California';
-- Use a subquery to filter cities in California
SELECT * FROM @database.cities
WHERE state_id = (SELECT id FROM @database.states WHERE name = 'California')
ORDER BY id ASC;
