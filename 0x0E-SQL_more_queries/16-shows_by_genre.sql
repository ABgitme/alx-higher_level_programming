SELECT t.title, g.name  -- Select the title from tv_shows and the name from tv_genres
FROM tv_shows t  -- Alias tv_shows table as t
LEFT JOIN tv_show_genres s ON t.id = s.show_id  -- Left join tv_show_genres table as s based on show_id
LEFT JOIN tv_genres g ON s.genre_id = g.id  -- Left join tv_genres table as g based on genre_id
ORDER BY t.title, g.name;  -- Order the results by show title and genre name
