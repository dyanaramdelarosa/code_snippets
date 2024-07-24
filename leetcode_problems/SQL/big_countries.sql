-- Problem Link: https://leetcode.com/problems/big-countries/
-- Author: Dyanara Dela Rosa
-- Date: July 24, 2024


-- Write your PostgreSQL query statement below
select "name", "population", area
from world
where area >= 3000000 or 
"population" >= 25000000