# Write your MySQL query statement below
select product_name,sum(unit) unit
from Products p inner join Orders o on p.product_id=o.product_id
where date_format(order_date,'%Y-%m')='2020-02'
group by product_name
having sum(unit)>=100



