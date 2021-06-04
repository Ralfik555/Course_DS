----------------------------------------------------------------------------
-- Zadanie 1
--
-- Policz sumę kroczącą (ang. rolling sum) wniosków dla kolejnych lat.
with wnioski_lata as (
 select id,
        opoznienie,
        kwota_rekompensaty_oryginalna as kwota,
        to_char(data_utworzenia, 'YYYY') as rok
 from wnioski
)

select rok, count(1), sum(count(1)) over(order by rok)
from wnioski_lata
group by rok
order by rok



----------------------------------------------------------------------------
-- Zadanie 2
--
-- Przeanalizuj dane AirHelp.
-- Jaka jest średnia, minimalna, maksymalna wartość wypłaconych rekompensat?
-- Jaka jest mediana wypłaconych rekompensat?
-- Jakie jest P25 i P75 dla wypłaconych rekompensat?

-- Na początek sprawdźmy! jakie są możliwe stany wniosku - dla pewności
select distinct stan_wniosku from wnioski

-- A teraz rozwiązanie zadania ...
select min(kwota_rekompensaty) as minimalna,
      max(kwota_rekompensaty) as maksymalna,
      avg(kwota_rekompensaty) as srednia,
      percentile_disc(0.5) within group (order by kwota_rekompensaty) as mediana,
      percentile_disc(0.25) within group (order by kwota_rekompensaty) as p25,
      percentile_disc(0.75) within group (order by kwota_rekompensaty) as p75
from wnioski
where lower(stan_wniosku) like 'wyplacony%'



----------------------------------------------------------------------------
-- Zadanie 3
--
-- Ile wniosków otrzymało rekompensatę - użyj CASE i PERCENTILE_DISC
-- Poniżej P25?
-- Powyżej P75?
with percentyle as
(
   select percentile_disc(0.25) within group (order by kwota_rekompensaty) as p25,
          percentile_disc(0.5) within group (order by kwota_rekompensaty)  as p50,
          percentile_disc(0.75) within group (order by kwota_rekompensaty) as p75
   from wnioski
   where lower(stan_wniosku) like 'wyplacony%'
)

select
      count(case when kwota_rekompensaty < p25 then w.id end),
      count(case when kwota_rekompensaty > p75 then w.id end)
from wnioski w, percentyle p
where lower(w.stan_wniosku) like 'wyplacony%'

-- Wypisz listę wniosków, którym wypłacono rekompensatę powyżej p75.
with percentyle as
(
   select percentile_disc(0.25) within group (order by kwota_rekompensaty) as p25,
          percentile_disc(0.5) within group (order by kwota_rekompensaty)  as p50,
          percentile_disc(0.75) within group (order by kwota_rekompensaty) as p75
   from wnioski
   where lower(stan_wniosku) like 'wyplacony%'
)

select w.id, w.kwota_rekompensaty, p.p75
from wnioski w, percentyle p
where w.kwota_rekompensaty > p.p75
and lower(w.stan_wniosku) like 'wyplacony%'



----------------------------------------------------------------------------
-- Zadanie 4
--
-- Przygotuj dane do histogramu prezentującego liczność wniosków wypłaconych
-- dla 15 przedziałów wnioskowanej kwoty rekompensaty.
select width_bucket(kwota_rekompensaty, 0, 10000, 15) as bucket, count(1) as cnt
from wnioski
group by bucket
order by bucket



----------------------------------------------------------------------------
-- Zadanie 5 - powtórka prawie wszystkiego :)
--
-- Jeden z partnerów sugeruje, że wnioski są próbą wyłudzenia odszkodowania.
-- Przyjrzyjmy się bliżej danym!
--
-- Jaka jest dynamika miesięczna (MoM) liczby wniosków dla partnera tui w roku 2017?
with tui_2017 as
(
  select id, date_part('month', data_utworzenia) as miesiac
  from wnioski
  where lower(partner) like 'tui'
),
tui_zliczone_miesiecznie_2017 as
(
  select miesiac,
        count(id) as ilosc,
        lag(count(id)) over(order by miesiac) ilosc_poprzedni
  from tui_2017
  group by miesiac
  order by miesiac
)

select miesiac, ilosc,
      round((ilosc-ilosc_poprzedni)/ilosc_poprzedni::numeric, 2) as mom_ilosc
from tui_zliczone_miesiecznie_2017

-- Jak przedstawia się suma wypłaconych rekompensat dla kolejnych miesięcy,
-- jak to wygląda MoM dla tui?
with tui_2017 as
(
 select kwota_rekompensaty_oryginalna as kwota,
        date_part('month', data_utworzenia) as miesiac
 from wnioski
 where lower(partner) like 'tui'
),
tui_rekompensaty_miesiecznie_2017 as
(
 select miesiac,
        sum(kwota) as suma_miesiac,
        lag(sum(kwota)) over (order by miesiac) as suma_miesiac_poprzedni
 from tui_2017
 group by miesiac
 order by miesiac
)

select miesiac,
      suma_miesiac,
      round((suma_miesiac - suma_miesiac_poprzedni)/suma_miesiac_poprzedni::numeric,2) as mom_suma_kwota
from tui_rekompensaty_miesiecznie_2017

-- Jak kwota rekompensaty jest skorelowana z liczbą pasażerów
-- dla różnych typów podróży i typów wniosków?
-- Jak wygląda średnia, mediana i moda rekompensaty w tych grupach?
-- Analizujemy rok 2017.
select typ_podrozy, typ_wniosku,
      count(1) as liczba_wnioskow,
      corr(kwota_rekompensaty_oryginalna, liczba_pasazerow) as korelacja_kwota_liczba_pasazerow,
      avg(kwota_rekompensaty_oryginalna) as srednia_kwota,
      percentile_disc(0.5) within group (order by kwota_rekompensaty_oryginalna) as mediana,
      mode() within group (order by kwota_rekompensaty_oryginalna) as moda
from wnioski
where lower(partner) like 'tui' and date_part('year',data_utworzenia)=2017
group by typ_podrozy, typ_wniosku

-- Czy wnioski biznesowe są częściej oceniane przez operatora (procentowo)?
-- Porównaj lata 2016 i 2017.
select 2016, count(case when w.typ_podrozy like 'biz%' then w.id end)/count(1)::numeric as procent_biz
  from wnioski w
  join analiza_operatora a on w.id=a.id_wniosku
  where date_part('year', w.data_utworzenia) = 2016
union
select 2017, count(case when w.typ_podrozy like 'biz%' then w.id end)/count(1)::numeric as procent_biz
  from wnioski w
  join analiza_operatora a on w.id=a.id_wniosku
  where date_part('year', w.data_utworzenia) = 2017



----------------------------------------------------------------------------
-- Zadanie 6
--
-- Jak wygląda rozkład odpowiedzi od operatora w kontekście różnych zmiennych?
--
-- Dla poszczególnych grup dla zmiennych:
-- Opóźnienia (tabela wnioski, kolumna opoznienie)
--
-- Policz DB i DG

with zliczone_bad_good as (
  select
    w.opoznienie,
    count(1),
    count(case when lower(ao.status_odp) like 'odrzucony%' then w.id end) bad,
    count(case when lower(ao.status_odp) like 'zaakceptowany' then w.id end) good
  from wnioski w
  join analiza_operatora ao on ao.id_wniosku = w.id
  join podroze p ON w.id = p.id_wniosku
  join szczegoly_podrozy s2 ON p.id = s2.id_podrozy where s2.czy_zaklocony = true
  group by 1
  order by 2 desc
)

select
  *,
  bad / sum(bad) over()::numeric DB,
  good / sum(good) over()::numeric DG
from zliczone_bad_good
