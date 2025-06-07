SELECT
    y.SCORE,
    e.EMP_NO,
    e.EMP_NAME,
    e.POSITION,
    e.EMAIL
FROM (
    SELECT
        EMP_NO,
        SUM(SCORE) AS SCORE
    FROM
        HR_GRADE
    WHERE
        YEAR = 2022
    GROUP BY
        EMP_NO
) AS y
JOIN HR_EMPLOYEES e ON y.EMP_NO = e.EMP_NO
WHERE y.SCORE = (
    SELECT
        MAX(SUM_SCORE)
    FROM (
        SELECT
            EMP_NO,
            SUM(SCORE) AS SUM_SCORE
        FROM
            HR_GRADE
        WHERE
            YEAR = 2022
        GROUP BY
            EMP_NO
    ) AS scores
);

