-- Write your query below

SELECT DISTINCT c.title
FROM tv_program t
JOIN content c ON t.content_id = c.content_id
WHERE 
    program_date >= '2020-06-01' 
    AND program_date < '2020-07-01'
    AND kids_content = 'Y'
    AND content_type = 'Movies';