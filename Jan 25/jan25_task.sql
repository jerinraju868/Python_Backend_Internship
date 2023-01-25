use beinex_sql;

select * from Employee_table;

-----LIKE-----
select * from Employee_table where First_name like 'a%a';

-----GROUP BY-----
select count(emp_id) as emp_count, First_Name from Employee_table group by First_Name;

-----HAVING-----
select count(emp_id) as emp_count, First_Name from Employee_table group by First_Name having emp_count = 2;

-----CASE-WHEN-----
select case when age < 25 then 'Minor' else 'Major' end from Employee_table;

-----MIN-----
select min(age) from Employee_table;

-----MAX-----
select max(age) from Employee_table;

-----SUM-----
select sum(age) from Employee_table;

-----AVG-----
select avg(age) from Employee_table;



use training;

select * from Student_table;

-----LEFT JOIN-----
select s.*,d.* from Student_table s left join Department_table d on s.dept_id = d.dept_id;

-----RIGHT JOIN-----
select s.*,d.* from Student_table s right join Department_table d on s.dept_id = d.dept_id;

-----INNER JOIN-----
select s.*,d.* from Student_table s inner join Department_table d on s.dept_id = d.dept_id;

-----LENGTH-----
select length(email_id) from Student_table;

-----TRIM-----
select trim(' hello backend web developer   ');

-----CONCAT-----
select concat(First_Name,'-',Last_Name) from Student_table;

-----UPPER-----
select upper(First_Name) from Student_table;

-----LOWER-----
select lower(Last_Name) from Student_table;

NUMERICAL FUNCTIONS

-----ABS-----
select abs(age) from Student_table;

-----ROUND-----
select round(age) from Student_table;

-----CEIL-----
select age,ceil(age) from Student_table;

-----FLOOR-----
select age,floor(age) from Student_table;

-----SIGN-----
select age,sign(age) from Student_table;

-----MOD-----
select mod(5,3);

----CURRENT DATE----
select current_date;

-----EXTRACT-----
select extract(day from date'2017-1-1'), extract(month from date'2017-1-1'), extract(year from date'2017-1-1');

-----COALESCE-----
select age, coalesce(age,0) from Student_table;

-----GREATEST-----
select greatest(5,2,7,1,10);

-----LEAST-----
select least(5,2,7,1,10);

-----ISNULL-----
select isnull(age) from Student_table;