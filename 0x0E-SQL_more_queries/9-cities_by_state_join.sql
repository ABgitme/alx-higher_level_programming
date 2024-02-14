-- Select cities.id, cities.name, and states.name from the cities and states tables
-- Join the cities and states tables using cities.state_id = states.id
-- Display cities.id, cities.name, and states.name in each record
-- Sort the results in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
