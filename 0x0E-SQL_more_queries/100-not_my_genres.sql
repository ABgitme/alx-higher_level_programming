-- Retrieve distinct genre names for TV shows except those related to the show "Dexter"
SELECT DISTINCT g.name  -- Select distinct genre names from tv_genres
FROM tv_genres g  -- Alias tv_genres table as g
INNER JOIN tv_show_genres s ON g.id = s.genre_id  -- Join tv_show_genres table as s based on genre_id
INNER JOIN tv_shows t ON s.show_id = t.id  -- Join tv_shows table as t based on show_id
WHERE g.name NOT IN (  -- Filter out genres related to the show "Dexter"
    SELECT g.name  -- Select genre names from tv_genres
    FROM tv_genres g  -- Alias tv_genres table as g
    INNER JOIN tv_show_genres s ON g.id = s.genre_id  -- Join tv_show_genres table as s based on genre_id
    INNER JOIN tv_shows t ON s.show_id = t.id  -- Join tv_shows table as t based on show_id
    WHERE t.title = "Dexter"  -- Filter shows with the title "Dexter"
)
ORDER BY g.name;  -- Order the results by genre name
