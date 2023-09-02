SELECT m.member_name, r.review_text, date_format(r.review_date, "%Y-%m-%d")
FROM member_profile m
-- 프로필과 리뷰 정보 다 필요해서 join
INNER JOIN (
    SELECT *
    FROM rest_review 

    -- 가장 많은 리뷰 수를 가지고 있는 멤버들만 뽑음
    WHERE member_id in (
        SELECT member_id 
        FROM rest_review
        GROUP BY member_id

        -- 멤버 아이디 별로 그룹지었을 때, 그 리뷰 개수가 최대인 멤버만 뽑기
        HAVING count(*) = (

            -- 가장 많은 리뷰가 몇 개인지 뽑기
            SELECT count(*)
            FROM rest_review
            GROUP BY member_id
            ORDER BY count(*) desc
            LIMIT 1
        )
    )
) r
ON m.member_id = r.member_id
ORDER BY r.review_date, r.review_text