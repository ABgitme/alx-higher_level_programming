-- Select the state and calculate the maximum temperature for each state
SELECT state, MAX(value) AS max_temp
-- Specify the table to retrieve data from
FROM temperatures
-- Group the data by state to calculate the maximum temperature for each state
GROUP BY state
-- Order the results by state name in ascending order
ORDER BY state;
