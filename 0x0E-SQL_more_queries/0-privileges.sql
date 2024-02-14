-- Check if necessary information_schema table exists in your MySQL version
SELECT COUNT(*) AS table_exists
FROM information_schema.user_grants;

IF table_exists > 0 THEN
    -- List privileges for user_0d_1
    SELECT *
    FROM information_schema.user_grants
    WHERE user = 'user_0d_1' AND host = '%';
    -- List privileges for user_0d_2
    SELECT *
    FROM information_schema.user_grants
    WHERE user = 'user_0d_2' AND host = '%';
END IF;

