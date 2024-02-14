-- lists the number of records with the same score in the table second_table
-- using command
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;