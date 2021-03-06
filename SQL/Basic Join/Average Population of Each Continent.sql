--MySQL

select co.continent, floor(avg(ci.population)) as avg from city as ci
join country as co on co.code = ci.countrycode
group by co.continent;