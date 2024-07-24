-- Problem Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Author: Dyanara Dela Rosa
-- Date: July 24, 2024


-- Write your PostgreSQL query statement below
select name
from customer where 
referee_id != 2
or referee_id is null