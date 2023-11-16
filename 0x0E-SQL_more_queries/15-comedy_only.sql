-- Manipulate db and table
-- CODE below.
SELECT tv_shows.title FROM tv_genres INNER JOIN tv_show_genres
on tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON
tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
