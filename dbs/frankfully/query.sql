/*
There's several entries for people named Frank... what's the salary of the one making the least subtracted from the one making the most? You shouldn't need to round, but make sure the answer has two decimals.

*/

SELECT MAX(salary) FROM employees where name = "Frank"   -  SELECT MIN(salary) FROM employees where name = "Frank" 