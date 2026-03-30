-- Write your query below

SELECT student_id, exam_id, score
FROM (
    SELECT 
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS row_num
    FROM exam_results
) t
WHERE row_num = 1
ORDER BY student_id;