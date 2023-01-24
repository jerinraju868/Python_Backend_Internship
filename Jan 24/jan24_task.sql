use beinex_sql;

-----CREATE-----
create table Employee(emp_id int primary key, First_Name varchar(20) not null, Last_Name varchar(20), department varchar(250), location varchar(250), age int, email_id varchar(50), mobile varchar(15), username varchar(250), password varchar(250));

-----INSERT-----
insert into Employee values(001,'Abin','Thomas', 'IT', 'idukki', 20, 'abin@gmail.com', '9874563210', 'abin','abin');
insert into Employee values(002,'Alan','Thomas', 'HR', 'Kottayam', 25, 'alan@gmail.com', '9874563210', 'alan','alan');
insert into Employee values(003,'Binu','Biju', 'Data Science', 'Kollam', 30, 'binu@gmail.com', '9874563211', 'binu','binu');
insert into Employee values(004,'Biju','Thomas', 'Electrical', 'Pathanamthitta', 30, 'biju@gmail.com', '9874563212', 'biju','biju');
insert into Employee values(005,'Christy','Abel', 'HR', 'Kottayam', 21, 'christy@gmail.com', '9874563213', 'christy','christy');

insert into Employee values(006,'Delen','Saji', 'IT', 'Ernakulam', 23, 'delen@gmail.com', '9874563214', 'delen','delen');
insert into Employee values(007,'Elmy','Sebastian', 'civil', 'Trissur', 28, 'elmy@gmail.com', '9874563215', 'elmy','elmy');
insert into Employee values(008,'Febin','Issac', 'Data Science', 'Kollam', 33, 'febin@gmail.com', '9874563216', 'febin','febin');
insert into Employee values(009,'Febin','Peter', 'Data Analyst', 'Pathanamthitta', 50, 'Febin@gmail.com', '9874563217', 'febinpeter','febinpeter');
insert into Employee values(010,'Ganeesh','Shiva', 'HR', 'Alappuzha', 29, 'ganeesh@gmail.com', '9874563218', 'ganeesh','ganeesh');

insert into Employee values(011,'Hari','Shivaji', 'IT', 'Tamil Nadu', 32, 'hari@gmail.com', '9874563219', 'hari','hari');
insert into Employee values(012,'Irshad','Rasheed', 'Counsilig', 'Telungana', 28, 'irshad@gmail.com', '9874563220', 'irshad','irshad');
insert into Employee values(013,'Jerin','', 'Software Developer', 'Delhi', 28, 'jerin@gmail.com', '9874563221', 'jerin','jerin');
insert into Employee values(014,'Merin','Raju', 'Data Analyst', 'Haryana', 24, 'merin@gmail.com', '9874563222', 'merin','merin');
insert into Employee values(015,'Sherin','Raju', 'HR', 'Bangalore', 25, 'sherin@gmail.com', '9874563223', 'sherin','sherin');
insert into Employee values(016,'Joby','Jose', 'HR', 'Bangalore', null, 'joby@gmail.com', '9874563224',null, null);


-----SELECT-----
select * from Employee;

-----DISTINCT-----
select distinct(age) from Employee;

-----WHERE-----
select First_Name,age from Employee where age <= 25;

-----AND-----
select * from Employee where First_Name = 'Febin' and age = 33;

-----OR------
select * from Employee where First_Name = 'Febin' or age =50;

-----NOT-----
select * from Employee where NOT age < 31;

-----ORDER BY------
select * from Employee order by First_Name desc;
select * from Employee order by age asc;

-----NULL-----
select * from Employee where age is null;
select * from Employee where username is null;


-----NOT NULL-----
select * from Employee where username is not null;

-----UPDATE-----
update Employee set email_id = 'jerinraju@gmail.com' WHERE emp_id = 013;


-----DELETE-----
delete from Employee where emp_id = 009;

-----LIMIT-----
select * from Employee limit 5;

-----COUNT-----
select count(First_name) from Employee where mobile = '9874563210';
select count(First_name) from Employee where age = 28;

-----IN-----
select * from Employee where age IN (20,25,30,35);

-----BETWEEN-----
select * from Employee where age BETWEEN 27 AND 35;