-- 4-first_table.sql

USE hbtn_0c_0;

-- Check if the table already exists before creating it
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Optionally, you can add a comment to describe the table
COMMENT ON TABLE first_table IS 'Table with id and name columns';
