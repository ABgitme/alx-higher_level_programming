-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS DATABASE().second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Insert multiple rows into the second_table table
INSERT INTO DATABASE().second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
