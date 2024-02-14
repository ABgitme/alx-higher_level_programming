-- Select tv_shows.title and tv_show_genres.genre_id from tv_shows and tv_show_genres tables
-- LEFT JOIN tv_show_genres on tv_shows.id = tv_show_genres.tv_show_id to include shows with no genre
-- Filter records where tv_show_genres.genre_id is NULL, indicating no genre linked
-- Display tv_shows.title and tv_show_genres.genre_id in each record, showing NULL if no genre exists
-- Sort the results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
