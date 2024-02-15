-- Select the city ID and name from the cities table
-- Join the cities and states tables based on the state_id and id columns, respectively
-- Filter the rows to include only cities from the state of California
-- Order the result set by the city ID in ascending order
SELECT c.id, c.name
FROM cities AS c
JOIN states AS s ON c.state_id = s.id
WHERE s.name = "California"
ORDER BY c.id;
