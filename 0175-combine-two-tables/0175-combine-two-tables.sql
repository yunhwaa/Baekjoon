# Write your MySQL query statement below
SELECT firstName, lastName, city, state
From Person 
LEFT JOIN ADDRESS
ON Person.personId = ADDRESS.personId;