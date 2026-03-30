-- Write your query below

SELECT DISTINCT title
FROM tv_program t
LEFT JOIN content c ON c.content_id = t.content_id
WHERE program_date >= '2020-06-01' 
    AND program_date < '2020-07-01'
    AND kids_content = 'Y'
    AND content_type = 'Movies'