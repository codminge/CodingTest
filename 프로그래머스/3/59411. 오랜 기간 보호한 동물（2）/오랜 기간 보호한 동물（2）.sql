-- 코드를 입력하세요
SELECT *
FROM (SELECT i.ANIMAL_ID, i.NAME
      FROM ANIMAL_INS i LEFT JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
      WHERE o.DATETIME IS NOT NULL
      ORDER BY o.DATETIME - i.DATETIME DESC)
WHERE ROWNUM < 3