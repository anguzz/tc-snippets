/*
As seen above, there's multiple entries for each name... what's the sum of the average salaries for each person's name? For example, the average of the Franks added with the average salary of every other name. Round this final answer to the nearest whole number.

 */ 

SELECT AVG(salary) FROM employees where group by name
