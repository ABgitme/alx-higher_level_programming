-- This query retrieves titles of "Comedy" TV shows.
SELECT t.`title`
-- From the 'tv_shows' table, aliased as 't'.
FROM `tv_shows` AS t
-- Use a subquery with EXISTS to efficiently check for "Comedy" genres.
WHERE EXISTS (
    -- This subquery checks if a show (t.id) has any "Comedy" (g.name) genres.
    SELECT 1
    FROM `tv_show_genres` AS s
    -- Join with 'tv_genres' (g) on genre ID (s.genre_id).
    INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
    -- Filter shows (t.id) and "Comedy" (g.name) genres.
    WHERE t.`id` = s.`show_id` AND g.`name` = "Comedy"
);
-- Order results by title in ascending order.
ORDER BY t.`title`;
