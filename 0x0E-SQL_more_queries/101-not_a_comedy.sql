-- Retrieve the title of all shows that don't have the genre Comedy
SELECT title
-- From the tv_shows table
FROM tv_shows
-- Filter the shows based on their IDs that are not associated with the Comedy genre
WHERE id NOT IN (
    -- Subquery to retrieve the IDs of shows associated with the Comedy genre
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (
        -- Subquery to retrieve the ID of the Comedy genre
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
)
-- Order the results in ascending order by the show title
ORDER BY title;
