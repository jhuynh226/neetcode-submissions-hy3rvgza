-- Write your query below
SELECT
    w.name AS warehouse_name,
    COALESCE(SUM(
        p.width * p.length * p.height * w.units
    ), 0) AS volume
FROM warehouse w
LEFT JOIN products p ON w.product_id = p.product_id
GROUP BY w.name;