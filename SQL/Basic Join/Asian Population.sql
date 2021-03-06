--MySQL

select sum(ci.population) from city as ci
join country as co on co.code = ci.countrycode
where continent = 'Asia';