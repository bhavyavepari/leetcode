# Write your MySQL query statement below
select product_id,year first_year, quantity,price from
sales where (product_id,year) in 
(select product_id,min(year)
over(partition by product_id) from Sales 
)