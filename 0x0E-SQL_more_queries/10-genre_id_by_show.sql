-- Store database name as a variable
SET @database = $database;

-- Select shows with at least one genre
SELECT s.title, g.genre_id
FROM @database.tv_shows AS s
INNER JOIN @database.tv_show_genres AS g ON s.id = g.show_id
GROUP BY s.title
HAVING COUNT(g.genre_id) >= 1
ORDER BY s.title ASC, g.genre_id ASC;
