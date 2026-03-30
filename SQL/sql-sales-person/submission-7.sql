-- Write your query below

SELECT s.name
FROM sales_person s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    LEFT JOIN company c ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
        AND s.sales_id = o.sales_id
);