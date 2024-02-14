-- Retrieve the titles of TV shows and their corresponding genres
SELECT t.title  -- Select the title from tv_shows
FROM tv_shows t  -- Alias tv_shows table as t
INNER JOIN tv_show_genres s ON t.id = s.show_id  -- Join tv_show_genres table as s based on show_id
INNER JOIN tv_genres g ON g.id = s.genre_id  -- Join tv_genres table as g based on genre_id
WHERE g.name = "Comedy"  -- Filter shows for the genre "Comedy"
ORDER BY t.title;  -- Order the results by show title
