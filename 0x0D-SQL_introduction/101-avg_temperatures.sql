-- SQL script that imports table dump "temperatures.sql" into the database "hbtn_0c_0".
-- Display average temperature (Farhenheit) by city ordered by temperature.

SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
