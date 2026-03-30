-- Write your query below

SELECT s.name
FROM sales_person s
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM orders o
    LEFT JOIN company c ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
);