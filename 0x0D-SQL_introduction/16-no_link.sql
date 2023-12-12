-- Lists all records of the table second_table with a non-empty name value.
-- Records are ordered by descending score.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
