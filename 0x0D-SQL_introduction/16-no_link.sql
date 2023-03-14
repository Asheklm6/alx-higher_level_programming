-- script that lists all records of the table
-- DML query
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
