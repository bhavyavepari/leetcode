WITH Sales AS (
    SELECT 
        u.product_id, 
        u.purchase_date, 
        u.units, 
        p.price
    FROM UnitsSold u
    JOIN Prices p 
    ON u.product_id = p.product_id 
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
)
SELECT 
    s.product_id, 
    ROUND(SUM(s.units * s.price) / NULLIF(SUM(s.units), 0), 2) AS average_price
FROM Sales s
GROUP BY s.product_id
UNION
SELECT 
    p.product_id, 
    0 AS average_price
FROM Prices p
WHERE p.product_id NOT IN (SELECT DISTINCT product_id FROM UnitsSold);
