-- Pass Fail Count

SELECT
status,
COUNT(*) AS total_students
FROM fact_exam_results
GROUP BY status;

------------------------------------------------

-- Department Wise Average

SELECT
department,
AVG(total) AS avg_marks
FROM fact_exam_results
GROUP BY department;

------------------------------------------------

-- Top Performers

SELECT
name,
department,
total
FROM fact_exam_results
ORDER BY total DESC;

------------------------------------------------

-- Gender Wise Performance

SELECT
gender,
AVG(total)
FROM fact_exam_results
GROUP BY gender;

-----------------------------------------------
---portfolio query

SELECT
department,
COUNT(*) AS total_students,
ROUND(AVG(total),2) AS average_marks,
MAX(total) AS highest_marks,
MIN(total) AS lowest_marks
FROM fact_exam_results
GROUP BY department;