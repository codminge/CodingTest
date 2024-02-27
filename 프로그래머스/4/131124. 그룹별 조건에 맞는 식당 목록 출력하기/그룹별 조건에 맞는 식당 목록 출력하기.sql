-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, TO_CHAR(REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE m INNER JOIN REST_REVIEW r ON m.MEMBER_ID = r.MEMBER_ID
WHERE MEMBER_NAME IN (SELECT MEMBER_NAME
                      FROM MEMBER_PROFILE m INNER JOIN REST_REVIEW r ON m.MEMBER_ID = r.MEMBER_ID
                      GROUP BY MEMBER_NAME
                      HAVING COUNT(MEMBER_NAME) IN (SELECT MAX(COUNT_NAME)
                                                    FROM (SELECT MEMBER_NAME, COUNT(MEMBER_NAME) AS COUNT_NAME
                                                          FROM MEMBER_PROFILE m INNER JOIN REST_REVIEW r ON m.MEMBER_ID = r.MEMBER_ID
                                                          GROUP BY MEMBER_NAME)))
ORDER BY review_date, review_text
