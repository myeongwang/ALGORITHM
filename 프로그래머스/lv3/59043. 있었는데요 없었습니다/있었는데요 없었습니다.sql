SELECT A.ANIMAL_ID,A.NAME
FROM ANIMAL_INS AS S LEFT JOIN ANIMAL_OUTS AS A 
ON S.NAME =A.NAME AND S.ANIMAL_ID = A.ANIMAL_ID AND S.ANIMAL_TYPE = A.ANIMAL_TYPE  
WHERE S.DATETIME> A.DATETIME 
ORDER BY S.DATETIME ASC