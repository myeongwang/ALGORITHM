SELECT PRODUCT_ID,PRODUCT_NAME,PRODUCT_CD,CATEGORY,PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1

/*
select *
from food_product
where price = (SELECT max(price) as price from food_product);
*/