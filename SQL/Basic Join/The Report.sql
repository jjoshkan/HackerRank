--MySQL

select
    case
        when g.grade < 8 then NULL
        else s.name
    end as Name,
    g.grade,
    s.marks
from students as s join grades as g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name, s.marks;