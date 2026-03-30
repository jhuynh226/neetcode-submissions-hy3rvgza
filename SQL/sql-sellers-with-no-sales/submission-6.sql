-- Write your query below

SELECT seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE 
        sale_date >= '2020-01-01' 
        AND sale_date < '2021-01-01'
        AND s.seller_id = o.seller_id
)
ORDER BY seller_name