with na as
(select
       year, sport, sex, count(*) lp,  sum(case when height = 'NA' or weight = 'NA' then 0 else 1 end) no_na,
       avg(case when height = 'NA' or weight = 'NA' then 1 else 0 end) proc_na
from (select id, year, sex, sport,height ,weight from  athlete_events a group by id, year, sport,height ,weight, sex) a
group by year, sport, sex),

mediany as
(select a.year, a.sport, a.sex,
percentile_cont(0.5) within group (order by cast( case when height != 'NA' then height end as float)) median_height,
percentile_cont(0.5) within group (order by cast( case when weight != 'NA' then weight end as float)) median_weight
from (select id, year, sex, sport,height ,weight from  athlete_events a group by id, year, sport,height ,weight, sex) a
join na on na.year = a.year and na.sport = a.sport and a.sex = na.sex
where na.proc_na < 0.5
and no_na >= 10
group by a.year, a.sport, a.sex),

###-------------- to jest zbiór do eksportu do Tableu  ------

baza as
(select a.*, weight/(height/100)^2 bmi
from
(select
id,
name,
a.sex,
age,
case when height = 'NA' then median_height else cast(height as float) end height,
case when weight = 'NA' then median_weight else cast(weight as float) end weight,
team,
noc,
games,
a.year,
season,
city,
a.sport,
event,
medal
from athlete_events a
join mediany m on m.year = a.year and m.sport = a.sport and m.sex = a.sex)a)

select * from
(select
*, rank()over(partition by sex order by std_bmi desc ) rk
  from
  (select
  sex, sport,
  stddev_pop(avg_bmi) std_bmi
  from
    (select year, sex, sport, avg(bmi) avg_bmi
    from (select sex, sport, year, id , bmi from baza ) b
    group by year, sex, sport)b
  group by sex, sport) s)r
where rk = 1

###---------- mój link do Dashboardu Tableu ----

https://public.tableau.com/profile/kglapiak#!/vizhome/BMI_17/Dashboard1?publish=yes