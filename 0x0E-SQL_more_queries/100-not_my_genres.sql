-- t
-- u
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.genre_id
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter' && tv_show_genres.genre_id = tv_genres.id
)
ORDER BY tv_genres.name ASC;