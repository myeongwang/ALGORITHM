/*
SELECT BOOK_ID, AUTHOR_NAME,PUBLISHED_DATE
FROM BOOK INNER JOIN AUTHOR ON BOOK.AUTHOR_ID=AUTHOR.AUTHOR_ID 
WHERE BOOK.CATEGORY = '경제'
GROUP BY BOOK.BOOK_ID
ORDER BY PUBLISHED_DATE 
*/

SELECT 
    BO.BOOK_ID, 
    AU.AUTHOR_NAME, 
    DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM AUTHOR AU 
INNER JOIN BOOK BO
 ON AU.AUTHOR_ID = BO.AUTHOR_ID
WHERE BO.CATEGORY LIKE '경제'
ORDER BY BO.PUBLISHED_DATE ASC;