----------------------------------------------------------------------------
-- Zadanie 1
--
-- Klienci AirHelp składają wnioski za pośrednictwem różnych kanałów komunikacji.
-- Jakie są możliwe kanały komunikacji?
select distinct kanal from wnioski;

-- Ile wniosków złożono z użyciem poszczególnych kanałów?
select kanal, count(id) from wnioski
group by kanal;


-- Podaj listę klientów (email), którzy kontaktowali się za pośrednictwem więcej
-- niż jednego kanału.
with email_kanal as
(
   select distinct kl.email, w.kanal
   from klienci kl
   join wnioski w ON kl.id_wniosku = w.id
   group by kl.email, w.kanal
)

select email from email_kanal
group by email
having count(1) > 1;

-- *** Podaj listę klientów (email), których kanał ostatnio utworzonego wniosku,
-- różni się od ich pierwszego kanału komunikacji
--
-- wyjaśnienie odnośnie parametrów range:
-- https://www.postgresql.org/docs/9.3/functions-window.html (komentarz pod tabelką).
with moje_dane as (
  select
    distinct kl.email,
    first_value(w.kanal) over(PARTITION BY kl.email order by w.data_utworzenia asc range between unbounded preceding and unbounded following) pierwszy_kanal,
    last_value(w.kanal) over(PARTITION BY kl.email order by w.data_utworzenia asc range between unbounded preceding and unbounded following) ostatni_kanal
  from klienci kl
  join wnioski w ON kl.id_wniosku = w.id
)

select *
from moje_dane
where pierwszy_kanal <> ostatni_kanal;



----------------------------------------------------------------------------
-- Zadanie 2
--
-- Wypiszmy listę tras z największą liczbą wniosków.
-- Wykluczamy wnioski, które mają przypisane więcej niż jedną podróż.
--
-- Stwórz listę wniosków (id) wraz z miejscem wylotu i miejscem docelowym podróży
with interesujace_id_wniosku as
(
   select id_wniosku, count(1)
   from szczegoly_podrozy sz,
        podroze p
   where sz.id_podrozy = p.id
   group by id_wniosku
   having count(1) = 1
)

select i.id_wniosku, s.kod_wyjazdu, s.kod_przyjazdu
from interesujace_id_wniosku i
join podroze p on p.id_wniosku=i.id_wniosku
join szczegoly_podrozy s on p.id = s.id_podrozy
order by 1;

-- Stwórz listę najpopularniejszych par miejsce-wylotu i miejsce-docelowe.
with interesujace_id_wniosku as
(
   select id_wniosku, count(1)
   from szczegoly_podrozy sz,
        podroze p
   where sz.id_podrozy = p.id
   group by id_wniosku
   having count(1) = 1
),
dane_wnioski as
(
   select i.id_wniosku, s.kod_wyjazdu, s.kod_przyjazdu
   from interesujace_id_wniosku i
   join podroze p on p.id_wniosku=i.id_wniosku
   join szczegoly_podrozy s on p.id = s.id_podrozy
)

select kod_wyjazdu, kod_przyjazdu, count(1)
from dane_wnioski
group by kod_wyjazdu, kod_przyjazdu
order by 3 desc;

--- *** Zrób listę najpopularniejszych tras, biorąc pod uwagę również wnioski
-- z kilkoma podróżami.
with dane_wnioski as
(
  select distinct
    p.id_wniosku as id_wniosku,
    first_value(s.kod_wyjazdu) over(partition by id_wniosku order by s.data_wyjazdu, s.data_utworzenia, s.data_aktualizacji range between unbounded preceding and unbounded following) miejsce_wyjazdu,
    last_value(s.kod_przyjazdu) over(partition by id_wniosku order by s.data_wyjazdu, s.data_utworzenia, s.data_aktualizacji range between unbounded preceding and unbounded following) miejsce_przyjazdu
  from podroze p
  join szczegoly_podrozy s on p.id = s.id_podrozy
  order by 1
)

select miejsce_wyjazdu, miejsce_przyjazdu, count(1)
from dane_wnioski
group by miejsce_wyjazdu, miejsce_przyjazdu
order by 3 desc;



----------------------------------------------------------------------------
-- Zadanie 3
--
-- (Aby poniższe zapytania działały, należy zaimportować plik
-- z danymi gapminder!)
--
-- Wypisz dane dla roku 2015 z tabeli gapminder
select * from gapminder
where year = 2015;

-- Wypisz dane odnośnie średniej długości życia, średniego przychodu
-- oraz sumaryczną populację dla regionów w roku 2015
select region, avg(life), avg(income), sum(population) from gapminder
where year = 2015
group by region;

-- Wypisz dane dla Polski, wzbogaconą o zmianę procentową w przychodzie YearOverYear
-- (dla wszystkich lat)
with data_poland as
(
  select
    year, life, population,
    income,
    lag(income) over() as last_year_income
  from gapminder
  where country = 'Poland'
  order by year
)

select *, round((income-last_year_income)/last_year_income,2) as YoY_income_change
from data_poland
order by year;



----------------------------------------------------------------------------
-- Zadanie 4
--
-- (Aby poniższe zapytania działały, należy zaimportować plik
-- z danymi gapminder!)
--
-- Wypisz dane dla roku 2015 dla krajów z regionu Europa …
select * from gapminder
where lower(region) like 'europe%'
and year = 2015
order by country asc;

-- Wypisz dane dla 2015 r. wzbogacone o informację o bieżącym procentowym
-- przyroście oczekiwanej długości życia (life) oraz przychodu
-- rok do roku (income) (Year Over Year)
with zmiany_gapminder as
(
   select country,
          life,
          income,
          year,
          (life - lag(life) over (partition by country order by year))
            / lag(life) over (partition by country order by year) as yoy_life,
          (income - lag(income) over (partition by country order by year))
            / lag(income) over (partition by country order by year) as yoy_income
   from gapminder
   where lower(region) like 'europe%'
   order by year
)

select
  country, life, income,
  yoy_life as YoY_life_2015,
  yoy_income as YoY_income_2015
from zmiany_gapminder
where year = 2015
order by country asc;

