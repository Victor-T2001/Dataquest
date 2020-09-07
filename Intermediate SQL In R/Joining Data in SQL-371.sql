## 1. Introducing Joins ##

SELECT *
FROM facts
INNER JOIN cities ON facts.id = cities.facts_id
LIMIT 10;


## 2. Understanding Inner Joins ##

SELECT c.*, f.name as country_name FROM facts as f
INNER JOIN cities as c on c.facts_id = f.id
limit 5

## 3. Practicing Inner Joins ##

SELECT f.name as country, c.name as capital_city FROM cities as c
INNER JOIN facts as f on f.id = c.facts_id
where c.capital = 1

## 4. Left Joins ##

select f.name as country, f.population FROM facts as f
LEFT JOIN cities as c ON f.id=c.facts_id
where c.name is NULL


## 6. Finding the Most Populous Capital Cities ##

SELECT c.name capital_city, f.name country, c.population population FROM cities as c
INNER JOIN facts as f on f.id=c.facts_id
WHERE c.capital = 1
ORDER BY population DESC
LIMIT 10

## 7. Combining Joins with Subqueries ##

SELECT c.name capital_city, f.name country, c.population population 
from facts as f
INNER JOIN (
    SELECT * FROM cities
    WHERE population>10000000
    AND capital = 1
    ) as c on c.facts_id=f.id
ORDER BY population DESC

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT * FROM 
(SELECT f.name country, SUM(c.population) urban_pop, f.population total_pop,
SUM(c.population)/CAST(f.population as FLOAT) urban_pct 
FROM facts as f
INNER JOIN cities as c ON f.id = c.facts_id
GROUP BY country
ORDER BY urban_pct)
WHERE urban_pct > 0.5