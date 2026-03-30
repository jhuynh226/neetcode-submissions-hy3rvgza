-- Write your query below

SELECT c.customer_id, c.name
FROM orders o
LEFT JOIN product p ON p.product_id = o.product_id
LEFT JOIN customers c ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING
    SUM(CASE 
        WHEN order_date >= '2020-06-01' AND order_date < '2020-07-01'
        THEN price * quantity
        ELSE 0
        END
    ) >= 100
    AND
    SUM(CASE 
        WHEN order_date >= '2020-07-01' AND order_date < '2020-08-01'
        THEN price * quantity
        ELSE 0
        END
    ) >= 100