-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
# 2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수
WHERE (CONV(GENOTYPE, 10, 2) LIKE "%1"
    OR CONV(GENOTYPE, 10, 2) LIKE "%1__")
    AND CONV(GENOTYPE, 10, 2) NOT LIKE "%1_";  
