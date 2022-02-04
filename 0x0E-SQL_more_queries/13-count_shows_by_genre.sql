-- lists all genres and number of shows in each genre.

SELECT tv_genres.name as genre, COUNT(tv_show_genres.id) as number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
