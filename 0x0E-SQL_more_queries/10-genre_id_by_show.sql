-- Select tv_shows.title and tv_show_genres.genre_id from tv_shows and tv_show_genres tables
-- Join tv_shows and tv_show_genres tables using tv_shows.id = tv_show_genres.tv_show_id
-- Filter records to include only shows that have at least one genre linked
-- Display tv_shows.title and tv_show_genres.genre_id in each record
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
