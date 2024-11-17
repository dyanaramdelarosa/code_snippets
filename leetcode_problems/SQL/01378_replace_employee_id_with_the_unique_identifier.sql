-- Problem Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Author: Dyanara Dela Rosa
-- Date: August 1, 2024


-- Write your PostgreSQL query statement below
select unique_id, "name"
from Employees e
left join EmployeeUNI eu
on e.id = eu.id