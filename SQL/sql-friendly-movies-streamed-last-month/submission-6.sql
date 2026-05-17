-- Write your query below

SELECT DISTINCT c.title
FROM tv_program tv
LEFT JOIN content c ON tv.content_id = c.content_id
WHERE
    program_date >= '2020-06-01' AND program_date < '2020-07-01' AND
    content_type = 'Movies' AND
    kids_content = 'Y';