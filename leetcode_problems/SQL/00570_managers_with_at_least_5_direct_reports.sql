-- Problem Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
-- Author: Dyanara Dela Rosa
-- Date: July 23, 2024

# Write your MySQL query statement below
select m.name
from employee e
join employee m
on e.managerId = m.id
group by e.managerId
having count(e.managerId) >= 5