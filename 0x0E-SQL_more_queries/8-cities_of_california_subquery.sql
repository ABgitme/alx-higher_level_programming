-- Store database name as a variable for flexibility
SET @database = $database;

-- Find California state's ID (handles multiple states with same name)
SELECT id FROM @database.states WHERE name = 'California';

-- If California exists, filter and sort cities accordingly
IF @@rowcount > 0 THEN
  SELECT * FROM @database.cities
  WHERE state_id IN (
    SELECT id FROM @database.states WHERE name = 'California'
  )
  ORDER BY id ASC;
ELSE
  -- Handle the case where there is no California state
  SELECT NULL AS id, NULL AS name;
END IF;
