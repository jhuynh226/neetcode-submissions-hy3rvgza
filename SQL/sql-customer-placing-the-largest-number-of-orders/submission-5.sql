-- Write your query below
SELECT customer_number 
FROM (
    SELECT customer_number, COUNT(*) AS orders_count
    FROM orders
    GROUP BY customer_number
    ORDER BY orders_count DESC
    LIMIT 1
);