-- SQL script that lists all cities of Califonia in the database "hbtn_0d_usa"
-- sort in ascending order by hbtn_0d_usa.cities.id

SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California');
