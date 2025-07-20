USE sale_and_product_manager;
create table sales  (
id int primary key auto_increment,
coustomer_id int,
product_id int,
quanty int,
sale_date datetime,
price decimal(10,2),
foreign key (coustomer_id) references coustomer (id),
foreign key (product_id) references product(product_id));
select * from sales;