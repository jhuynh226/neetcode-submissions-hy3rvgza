-- Write your query below

SELECT s.id, name
FROM students s
WHERE s.department_id NOT IN (
    SELECT d.id
    FROM departments d
) OR s.department_id IS NULL;