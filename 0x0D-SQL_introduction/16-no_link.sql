-- lists all records of the table second_table
-- using command
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;