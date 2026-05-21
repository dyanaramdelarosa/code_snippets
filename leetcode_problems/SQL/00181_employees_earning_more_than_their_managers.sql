-- Problem Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- Author: Dyanara Dela Rosa
-- Date: May 21, 2026


select e1.name as Employee
from Employee as e1
inner join Employee as e2
on e1.managerId = e2.id
where e1.salary > e2.salary

-- select e.name as Employee from Employee as e
-- where e.salary > (select e2.salary from Employee as e2 where e2.id = e.managerId)
