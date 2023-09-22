# Write your MySQL query statement below

SELECT Name as customers from Customers
WHERE Id NOT IN (SELECT CustomerId from Orders)