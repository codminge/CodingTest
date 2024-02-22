-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
CASE WHEN STATUS = 'DONE' THEN '거래완료'
     WHEN STATUS = 'SALE' THEN '판매중'
     WHEN STATUS = 'RESERVED' THEN '예약중' END STATUS
FROM USED_GOODS_BOARD
WHERE TO_CHAR(CREATED_DATE, 'YYYY-MM-DD') = '2022-10-05'
ORDER BY BOARD_ID DESC