## 3. The With Clause ##

WITH subquery AS
    (
        SELECT
            pl.playlist_id playlist_id,
            pl.name playlist_name,
            t.name track_name,
            (t.milliseconds / 1000) track_length
        FROM playlist pl
        LEFT JOIN playlist_track plt ON pl.playlist_id = plt.playlist_id  
        LEFT JOIN track t ON plt.track_id = t.track_id
    )
    
SELECT 
    playlist_id, 
    playlist_name,
    COUNT(track_name) number_of_tracks,
    SUM(track_length) length_seconds
FROM subquery
GROUP BY playlist_id
ORDER BY 1

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.* FROM chinook.customer c
    INNER JOIN chinook.invoice i ON i.customer_id = c.customer_id
    GROUP BY c.customer_id
    HAVING SUM(i.total) > 90;

SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * FROM customer_usa
UNION
SELECT * FROM customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

WITH customer_usa_gt_90_dollars AS
    (
    SELECT * FROM customer_usa
    INTERSECT 
    SELECT * FROM customer_gt_90_dollars
    )

SELECT 
    e.first_name || ' ' || e.last_name employee_name,
    COUNT(c.support_rep_id) customers_usa_gt_90
FROM employee e
LEFT JOIN customer_usa_gt_90_dollars c ON e.employee_id = c.support_rep_id
WHERE e.title = "Sales Support Agent"
GROUP BY 1
ORDER BY 1

## 7. Multiple Named Subqueries ##

WITH
    india AS 
        (
        SELECT * FROM customer
        WHERE country = "India"
        ),
    sum AS
        (
        SELECT 
            customer_id,
            SUM(total) total_purchases
        FROM invoice
        GROUP BY 1
        )
        
SELECT 
    i.first_name || ' ' || i.last_name customer_name,
    s.total_purchases
FROM india i
INNER JOIN sum s ON s.customer_id = i.customer_id
ORDER BY 1

## 8. Challenge: Each Country's Best Customer ##

WITH 
    customers as 
        (
        SELECT 
            c.country,
            c.first_name || ' ' || c.last_name customer_name,
            SUM(i.total) as total_purchases
        FROM customer c
        INNER JOIN invoice i ON c.customer_id = i.customer_id
        GROUP BY c.customer_id ORDER BY 1
        ),
     max_country AS
        (
        SELECT country, MAX(total_purchases) total_purchased FROM customers 
        GROUP BY country
        )
        
SELECT m.country, c.customer_name, m.total_purchased 
FROM max_country m
INNER JOIN customers c ON c.total_purchases = m.total_purchased
WHERE m.country = c.country