-- Select the top 3 cities' temperatures during July and August ordered by temperature descending
SELECT city, AVG(value) AS avg_temp
FROM temperatures
-- Filter records for July and August (months 7 and 8)
WHERE month IN (7, 8)
-- Group by city to calculate the average temperature
GROUP BY city
-- Order by average temperature in descending order
ORDER BY avg_temp DESC
-- Limit the results to the top 3 cities
LIMIT 3;
