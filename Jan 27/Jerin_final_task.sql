-----USING THE DATABASE-----
Use sql_final_task;

-----CREATING THE CUSTOMER TABLE-----
create table Jerin_Customer(customer_id varchar(10) primary key, customer varchar(20), region varchar(50));


-----INSERTING THE VALUES INTO THE CUSTOMER TABLE-----
insert into Jerin_Customer values('C1', 'Jones', 'East');
insert into Jerin_Customer values('C2', 'Kivell', 'Central');
insert into Jerin_Customer values('C3', 'Jardine', 'Central');
insert into Jerin_Customer values('C4', 'Gill', 'Central');
insert into Jerin_Customer values('C5', 'Sorvino', 'West');
insert into Jerin_Customer values('C6', 'Andrews', 'Central');
insert into Jerin_Customer values('C7', 'Thompson', 'West');
insert into Jerin_Customer values('C8', 'Morgan', 'Central');
insert into Jerin_Customer values('C9', 'Howard', 'East');
insert into Jerin_Customer values('C10', 'Parent', 'East');
insert into Jerin_Customer values('C11', 'Smith', 'Central');


-----RETRIVING THE DATA FROM THE TABLE-----
select * from Jerin_Customer;

-----CREATING THE SALES TABLE------
create table Jerin_Sales(sales_id int primary key, order_date date, customer_id varchar(10), item varchar(20) not null, units int, unit_cost double, total double);

select * from Jerin_Sales;

-----Combining the customer table and sales table----
create table Jerin_Combined (
select Jerin_Sales.customer_id, Jerin_Sales.sales_id, Jerin_Sales.item, Jerin_Sales.units, Jerin_Sales.unit_cost, Jerin_Sales.total, Jerin_Customer.customer, Jerin_Customer.region, Jerin_Sales.order_date
  from Jerin_Customer
  join Jerin_Sales
    on Jerin_Customer.customer_id = Jerin_Sales.customer_id) ;

-----Adding primary key to new table 
alter table Jerin_Combined add primary key(sales_id);

select * from Jerin_Combined;

-----Write a command to display first 10 row-----
select * from Jerin_Combined limit 10;

-----Identify unique items-----
select distinct(item) from Jerin_Combined;

-----Identify any unit cost is negative-----
select unit_cost,sign(unit_cost) from Jerin_Combined;

-----Identify minimum and maximum unit price happened for same item-----
select min(unit_cost),max(unit_cost) from Jerin_Combined;

-----Identify the Total sales happened in the year of 2021-----
select sum(Total) from Jerin_Combined where order_date between "2021-01-01" AND "2021-12-31";

-----Identify the region with highest and lowest sales------
select min(region), max(region) from Jerin_Combined;

-----Identify the customer name having highest sales for the year 2022-----
select max(customer) from Jerin_Combined where order_date between "2022-01-01" AND "2022-12-31";

-----Which item has highest and lowest unit cost-----
select min(unit_cost), max(unit_cost) from Jerin_Combined;

-----Identify items starts with letter 'P'-----
select * from Jerin_Combined where item like 'P%';

-----Filter the table having items Pen and Pencil-----
select * from Jerin_Combined where item in('Pen','Pencil');

-----Filter the table with unit cost between 1 and 100-----
select * from Jerin_Combined where unit_cost between 1 and 100;

-----Identify the customer with more no of transaction(no of entries)-----
select count(customer), customer from Jerin_Combined group by customer;

-----Identify which item has maximum sales in each region-----
select region,max(item) from Jerin_Combined group by region;