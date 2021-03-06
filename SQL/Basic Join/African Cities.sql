--MySQL

select ci.name from city as ci
join country as co on co.code = ci.countrycode
where co.continent = 'Africa';