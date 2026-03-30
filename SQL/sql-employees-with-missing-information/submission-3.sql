-- Write your query below

SELECT employee_id
FROM employees e
FULL JOIN salaries s USING (employee_id)
WHERE name IS NULL OR salary IS NULL;