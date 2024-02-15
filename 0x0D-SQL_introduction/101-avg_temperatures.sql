-- Select the city and calculate the average temperature (Fahrenheit) for each city
SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
-- Specify the table and database
FROM temperatures
-- Group the data by city
GROUP BY city
-- Order the results by the average temperature in descending order
ORDER BY avg_temperature_fahrenheit DESC;
