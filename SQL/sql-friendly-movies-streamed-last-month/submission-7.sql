-- Write your query below
SELECT DISTINCT title
FROM tv_program t
LEFT JOIN content c ON t.content_id = c.content_id
WHERE
    kids_content = 'Y' AND
    content_type = 'Movies' AND
    program_date >= '2020-06-01' AND program_date < '2020-07-01';