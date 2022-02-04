-- SQL script lists all shows contained in the database "hbtn_0d_tvshows"
--Display "tv_shows.title" and "tv_show_genres.genre_id"
-- Sorted in ascending order of "tv_shows.title" and "tv_show_genres.genre_id"

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
