--  This SQL query retrieves titles of shows (s.title) and their associated genre IDs (g.genre_id)
--  from the tv_shows (s) and tv_show_genres (g) tables.
--  An INNER JOIN ensures shows with linked genres are included.
--  Results are ordered alphabetically by title (s.title) and numerically by genre ID (g.genre_id) in ascending order.
SELECT s.title, g.genre_id
FROM tv_shows s
INNER JOIN tv_show_genres g ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id ASC;
