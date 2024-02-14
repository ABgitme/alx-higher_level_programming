-- Retrieve the names of TV genres for the show "Dexter"
SELECT g.name
FROM tv_genres g  -- Alias tv_genres table as g
INNER JOIN tv_show_genres s ON g.id = s.genre_id  -- Join tv_show_genres table as s based on genre_id
INNER JOIN tv_shows t ON t.id = s.show_id  -- Join tv_shows table as t based on show_id
WHERE t.title = "Dexter"  -- Filter the shows for the title "Dexter"
ORDER BY g.name;  -- Order the results by genre name
