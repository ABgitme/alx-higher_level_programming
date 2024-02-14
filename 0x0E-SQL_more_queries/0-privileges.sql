-- Select all rows from the mysql.db table
SELECT *
-- Filter rows where the User column matches 'user_0d_1' or 'user_0d_2'
FROM mysql.db
WHERE User IN ('user_0d_1', 'user_0d_2');
