-- Write your query below

SELECT
    name,
    SUM(amount) AS balance
FROM users u
LEFT JOIN transactions t ON u.account = t.account
GROUP BY u.account
HAVING SUM(amount) > 10000;