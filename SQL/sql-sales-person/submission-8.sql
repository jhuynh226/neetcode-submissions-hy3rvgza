-- Write your query below
SELECT name
FROM sales_person sp
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    LEFT JOIN company c on o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
);