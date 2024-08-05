-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', A.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE AS A
RIGHT JOIN (SELECT BOARD_ID
           FROM USED_GOODS_BOARD
           WHERE VIEWS IN (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)) AS B
ON A.BOARD_ID = B.BOARD_ID
ORDER BY FILE_ID DESC;
