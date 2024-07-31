-- Problem Link: https://leetcode.com/problems/invalid-tweets/
-- Author: Dyanara Dela Rosa
-- Date: July 24, 2024


-- Write your PostgreSQL query statement below
select tweet_id
from tweets
where length(content) > 15