--MySQL

select distinct city from station where city regexp '^[^aiueo]' or city regexp '[^aiueo]$';