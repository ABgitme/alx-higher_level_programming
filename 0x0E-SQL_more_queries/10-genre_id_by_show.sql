-- Store database name as a variable
SELECT 
  tv_shows.title,
  tv_show_genres.genre_id
FROM $database.tv_shows
INNER JOIN $database.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
