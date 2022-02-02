-- SQL script that imports table dump "temperatures.sql" into the database "hbtn_0c_0".
-- Display top 3 cities with highest average temperature (Farhenheit) between July and August ordered by temperature.

SELECT city, AVG(value) AS 'avg_temp' FROM temperatures WHERE month = 7 OR month = GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
