-- Problem Link: https://leetcode.com/problems/combine-two-tables/
-- Author: Dyanara Dela Rosa
-- Date: May 21, 2026

select firstName, lastName, city, state
from Person left join Address
on Person.personId = Address.personId