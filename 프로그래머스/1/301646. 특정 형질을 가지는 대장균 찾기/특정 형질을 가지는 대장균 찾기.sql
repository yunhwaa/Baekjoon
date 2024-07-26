-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (CONV(GENOTYPE, 10, 2) like '%1'
    OR CONV(GENOTYPE, 10, 2) like '%1__')
    AND CONV(GENOTYPE, 10, 2) not like '%1_';