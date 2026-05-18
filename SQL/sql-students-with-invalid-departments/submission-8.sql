-- Write your query below

-- SELECT s.id, s.name
-- FROM students s
-- LEFT JOIN departments d ON s.department_id = d.id
-- WHERE d.name IS NULL;

SELECT s.id, s.name
FROM students s
WHERE s.department_id NOT IN (
    SELECT id
    FROM departments
) OR s.department_id IS NULL;