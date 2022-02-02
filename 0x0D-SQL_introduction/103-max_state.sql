-- SQL script that imports table dump "temperatures.sql" into the database "hbtn_0c_0".
-- Display maximum temperature (Farhenheit) of each state ordered by state name.

SELECT state, MAX(value) AS 'max_temp' FROM temperatures GROUP BY state ORDER BY state DESC;
