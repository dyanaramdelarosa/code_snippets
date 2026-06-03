-- Problem Link: https://leetcode.com/problems/customers-who-never-order/
-- Author: Dyanara Dela Rosa
-- Date: June 3, 2026


select name as Customers
from customers
left join orders
on customers.id = orders.customerId
where orders.id is NULL