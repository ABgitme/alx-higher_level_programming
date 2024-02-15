-- Retrieve distinct titles of shows that are not in the Comedy genre
SELECT DISTINCT t.title
FROM tv_shows AS t
-- Left join with tv_show_genres to include all shows, even those without genres
LEFT JOIN tv_show_genres AS s ON s.show_id = t.id
-- Left join with tv_genres to check for shows in the Comedy genre
LEFT JOIN tv_genres AS g ON g.id = s.genre_id
-- Filter out shows that are in the Comedy genre
WHERE g.name IS NULL OR g.name != 'Comedy'
ORDER BY t.title;
