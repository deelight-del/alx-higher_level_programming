-- File that is used to manipulate second_table
-- The corresponding query for the above
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
