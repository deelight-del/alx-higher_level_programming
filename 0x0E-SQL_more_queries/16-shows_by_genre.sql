-- Manipulate db and table
-- CODE below.
SELECT tv_shows.title, tv_genres.name FROM
tv_shows LEFT OUTER JOIN 
(tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id)
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_genres.name ASC;
