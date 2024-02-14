-- Select all cities from the cities table
-- Filter cities based on the state_id obtained from the states table where the name is California
-- The id of California state is obtained from the states table
-- Cities are ordered in ascending order by cities.id
SELECT cities.*
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
