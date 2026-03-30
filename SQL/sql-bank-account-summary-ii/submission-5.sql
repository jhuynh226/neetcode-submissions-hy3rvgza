-- Write your query below

SELECT name, SUM(amount) AS balance 
FROM users u
JOIN transactions t ON t.account = u.account
GROUP BY t.account, u.name
HAVING SUM(amount) > 10000