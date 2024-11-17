-- Problem Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Author: Dyanara Dela Rosa
-- Date: July 24, 2024


-- Write your PostgreSQL query statement below
select product_id 
from products 
where low_fats = 'Y' and
recyclable = 'Y'