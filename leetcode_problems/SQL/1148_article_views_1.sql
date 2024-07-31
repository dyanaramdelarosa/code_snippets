-- Problem Link: https://leetcode.com/problems/article-views-i/
-- Author: Dyanara Dela Rosa
-- Date: July 24, 2024


-- Write your PostgreSQL query statement below
select distinct(author_id) as id
from views
where author_id = viewer_id
order by id