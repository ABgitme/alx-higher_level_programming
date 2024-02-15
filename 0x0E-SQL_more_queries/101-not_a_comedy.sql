-- Retrieve the title of all shows that don't have the genre Comedy
SELECT title
-- From the tv_shows table
FROM tv_shows
-- Left join with the tv_show_genres table to check if the show has the Comedy genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id IS NULL
-- Filter out the shows that have the Comedy genre
WHERE tv_show_genres.genre_id IS NULL
-- Order the results in ascending order by the show title
ORDER BY title;
