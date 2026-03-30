-- Write your query below

SELECT name, SUM(t.amount) AS balance
FROM users u
LEFT JOIN transactions t ON u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000;