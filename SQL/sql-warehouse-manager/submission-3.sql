-- Write your query below

SELECT 
    w.name AS warehouse_name,
    SUM(width * length * height * units) AS volume
FROM warehouse w
LEFT JOIN products p ON w.product_id = p.product_id
GROUP BY w.name