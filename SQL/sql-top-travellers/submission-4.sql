-- Write your query below

SELECT 
    u.name,
    CASE
        WHEN SUM(distance) IS NULL THEN 0
        ELSE SUM(distance)
    END AS travelled_distance
FROM users u
LEFT JOIN rides r ON r.user_id = u.id
GROUP BY r.user_id, name
ORDER BY travelled_distance DESC, u.name
