
with mth as
(select
 *, (avg_cena - lag(avg_cena)over(order by mth)) /  lag(avg_cena)over(order by mth) mom
from
(select date_trunc('month',to_date(data,'YYYY-MM-DD')) mth , avg(zamkniecie) avg_cena from xpdusd_d
group by 1 order by 1 ) c),

dates as
(select generate_series('2016-01-01'::date, '2019-12-01'::date, interval'1 month') as  data ),

merge_tab as
(select *, rank()over(partition by mth order by data) nr, avg(mom)over() trend,
sum(case when  mth = '2018-11-01'::date then avg_cena else 0 end)over()last_cena
from dates d
left join mth m on m.mth = d.data
order by 1)


select data, round(case when avg_cena is null then power(1 + trend,nr) * last_cena else avg_cena  end ,2) avg_cena
from
merge_tab




