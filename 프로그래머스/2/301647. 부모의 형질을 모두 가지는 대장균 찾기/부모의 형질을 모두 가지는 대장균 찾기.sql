-- 코드를 작성해주세요
SELECT T1.ID AS ID, T1.GENOTYPE AS GENOTYPE, T2.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS T1
LEFT JOIN ECOLI_DATA AS T2
ON T1.PARENT_ID = T2.ID
WHERE T1.GENOTYPE & T2.GENOTYPE = T2.GENOTYPE
ORDER BY T1.ID ASC;




