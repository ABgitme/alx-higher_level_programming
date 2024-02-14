-- Select the title from tv_shows and the genre_id from tv_show_genres
SELECT s.title, g.genre_id
-- Alias tv_shows table as s
FROM tv_shows s
-- Left join tv_show_genres table as g
LEFT JOIN tv_show_genres g
-- Match records where the id from tv_shows matches the show_id from tv_show_genres
ON s.id = g.show_id
-- Filter records where genre_id is NULL (i.e., no genre linked)
WHERE g.genre_id IS NULL
-- Order the results by title and genre_id in ascending order
ORDER BY s.title ASC, g.genre_id ASC;
