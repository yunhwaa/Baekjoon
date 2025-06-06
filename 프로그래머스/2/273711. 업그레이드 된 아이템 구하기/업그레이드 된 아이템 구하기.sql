-- 코드를 작성해주세요
# 업그레이드 된 아이템 구하기
# WHERE IN 함
# 특정 컬럼의 값이 주어진 목록에 속하는지 확인할 때 매우 유용
# 여러 값을 한 번에 비교할 수 있음

SELECT ITEM_INFO.ITEM_ID, ITEM_INFO.ITEM_NAME, RARITY
FROM ITEM_INFO,ITEM_TREE
WHERE ITEM_INFO.ITEM_ID = ITEM_TREE.ITEM_ID
    AND PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = "RARE")
ORDER BY ITEM_ID DESC;
