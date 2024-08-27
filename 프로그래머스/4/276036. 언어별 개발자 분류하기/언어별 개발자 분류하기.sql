-- 코드를 작성해주세요
SELECT CASE WHEN (SKILL_CODE &
                                    (SELECT SUM(CODE) 
                                    FROM SKILLCODES
                                    WHERE NAME = 'Python')) > 0
                AND (SKILL_CODE & 
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE CATEGORY = 'Front End')) > 0 THEN 'A'
            WHEN (SKILL_CODE & 
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE NAME = 'C#')) > 0 THEN 'B'
            WHEN (SKILL_CODE &
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE CATEGORY = 'Front End')) > 0 THEN 'C' 
        END AS GRADE,
ID, EMAIL
FROM DEVELOPERS
WHERE CASE WHEN (SKILL_CODE &
                                    (SELECT SUM(CODE) 
                                    FROM SKILLCODES
                                    WHERE NAME = 'Python')) > 0
                AND (SKILL_CODE & 
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE CATEGORY = 'Front End')) > 0 THEN 'A'
            WHEN (SKILL_CODE & 
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE NAME = 'C#')) > 0 THEN 'B'
            WHEN (SKILL_CODE &
                                    (SELECT SUM(CODE)
                                    FROM SKILLCODES
                                    WHERE CATEGORY = 'Front End')) > 0 THEN 'C' 
        END IS NOT NULL
ORDER BY GRADE, ID ASC;


# DEVELOPERS 테이블의 SKILL_CODE를 2진수로 바꾼 값이
# SKILLCODES의 CODE 값을 2진수로 바꾼 값