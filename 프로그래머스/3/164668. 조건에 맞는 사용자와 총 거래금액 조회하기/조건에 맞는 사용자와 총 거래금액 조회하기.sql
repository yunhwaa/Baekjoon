-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS BOARD, USED_GOODS_USER AS USER
WHERE BOARD.WRITER_ID = USER.USER_ID
    AND STATUS = 'DONE'
GROUP BY BOARD.WRITER_ID HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES ASC;