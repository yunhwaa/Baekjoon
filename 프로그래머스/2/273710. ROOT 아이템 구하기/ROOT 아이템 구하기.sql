-- 코드를 작성해주세요
SELECT T1.ITEM_ID, ITEM_NAME
FROM ITEM_INFO AS T1
LEFT JOIN ITEM_TREE AS T2
ON T1.ITEM_ID = T2.ITEM_ID
WHERE T2.PARENT_ITEM_ID IS NULL
ORDER BY T1.ITEM_ID;
