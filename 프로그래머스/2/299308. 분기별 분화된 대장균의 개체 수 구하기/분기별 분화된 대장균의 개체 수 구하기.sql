SELECT 
    CONCAT(quarter_num, 'Q') AS QUARTER,
    COUNT(*) AS ECOLI_COUNT
FROM (
    SELECT QUARTER(DIFFERENTIATION_DATE) AS quarter_num
    FROM ECOLI_DATA
) AS sub
GROUP BY quarter_num
ORDER BY quarter_num;
