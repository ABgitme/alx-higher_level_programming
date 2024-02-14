-- Select the name from tv_genres as genre
-- Count the number of occurrences and alias it as number_of_shows
-- Alias tv_genres table as g
-- Inner join tv_show_genres table as t on id and genre_id
-- Group the results by genre name
-- Order the results by the number of shows in descending order
SELECT g.name AS genre,
    COUNT(*) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres t ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
