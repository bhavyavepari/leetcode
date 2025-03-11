# Write your MySQL query statement below
select name,bonus from employee e left join Bonus b on e.empId=b.empid where b.bonus<1000 or bonus is null ;