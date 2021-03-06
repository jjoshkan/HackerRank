--MySQL

SELECT (months*salary) as earnings, count(*) as count_ from employee 
group by earnings order by earnings desc limit 1;