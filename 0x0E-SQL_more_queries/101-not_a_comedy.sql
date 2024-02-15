-- Select shows not linked to the "Comedy" genre (id: 5)
SELECT s.title
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
WHERE g.genre_id IS NULL OR g.genre_id != 5;
-- Order results by title in ascending order
ORDER BY s.title ASC;
