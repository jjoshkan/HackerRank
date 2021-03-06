--MySQL

select distinct city from station where city regexp '^[^aiueo].*[^aiueo]$';