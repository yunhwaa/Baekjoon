# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM ACTIVITY 
GROUP BY PLAYER_ID;