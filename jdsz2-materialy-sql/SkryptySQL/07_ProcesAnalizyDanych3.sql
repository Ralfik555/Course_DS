----------------------------------------------------------------------------
-- Zadanie 1
--
-- Jak wygląda rozkład odpowiedzi od operatora w kontekście różnych zmiennych?
--
-- Dla poszczególnych grup dla zmiennych:
-- Opóźnienia (tabela wnioski, kolumna opoznienie)
--
-- Policz Weight Of Evidence (WOE)

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
),
zliczone_db_dg as (
 select
   *,
   bad / sum(bad) over()::numeric DB,
   good / sum(good) over()::numeric DG
 from zliczone_bad_good
)

select *, ln(dg / db) as woe
from zliczone_db_dg



----------------------------------------------------------------------------
-- Zadanie 2
--
-- Jak wygląda rozkład odpowiedzi od operatora w kontekście różnych zmiennych?
--
-- Policz Information Value:
-- Opóźnienia (tabela wnioski, kolumna opoznienie)

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
),
zliczone_db_dg as (
 select
   *,
   bad / sum(bad) over()::numeric DB,
   good / sum(good) over()::numeric DG
 from zliczone_bad_good
),
zliczone_woe as (
 select *, ln(dg / db) as woe
 from zliczone_db_dg
)

select sum((dg-db)*woe) as IV from zliczone_woe



----------------------------------------------------------------------------
-- Zadanie 3
--
-- Stwórz zapytanie, które wyliczy średnią liczbę wniosków w danym dniu tygodniu.
-- Dla wyliczenia tej średniej użyj wniosków złożonych od 20.01.2018 włącznie.

with wnioski_w_dniu as (
  select to_char(data_utworzenia, 'YYYY-MM-DD')::date data_wniosku,
    count(1) ilosc_wnioskow
  from wnioski
  where data_utworzenia > '2018-01-20'
  group by 1
  order by 1
)

select to_char(data_wniosku, 'Day') as dzien,
  round(avg(ilosc_wnioskow)) as srednia_ilosc_wnioskow
from wnioski_w_dniu
group by 1
order by 1



----------------------------------------------------------------------------
-- Zadanie 4
--
-- Wypisz ilość utworzonych wniosków dla każdego dnia od 20.01.2018,
-- wraz z sumą skumuluwaną/kroczącą w kolejnych dniach.

with wnioski_w_dniu as (
   select to_char(data_utworzenia, 'YYYY-MM-DD')::date data_wniosku,
     count(1) as ilosc_wnioskow
   from wnioski
   where data_utworzenia > '2018-01-20'
   group by 1
   order by 1
),
prognoza_dni_tygodnia as (
   select to_char(data_wniosku, 'Day') as dzien,
     round(avg(ilosc_wnioskow)) as srednia_ilosc_wnioskow
   from wnioski_w_dniu
   group by 1
   order by 1
)
select w.data_wniosku,
  w.ilosc_wnioskow,
  sum(w.ilosc_wnioskow) over(order by w.data_wniosku) as suma_skumulowana
from wnioski_w_dniu w



----------------------------------------------------------------------------
-- Zadanie 5
--
-- Wygeneruj daty od 20.01.2018 włącznie do końca lutego 2018 roku.
--
-- Funkcja generate_series jako argumenty wymaga wartości typu
-- timestamp i interval!

-- rozwiązanie 1
select generate_series('2018-01-20'::date, '2018-02-28'::date, '1 day')::date as wygenerowana_data

-- rozwiązanie 2 - ilustrujące operacje na datach
select generate_series(
         '2018-01-20'::date,
         date_trunc('month', '2018-02-01'::date)+interval '1 month'-interval '1 day',
         '1 day'
       )::date as wygenerowana_data




----------------------------------------------------------------------------
-- Zadanie 6
--
-- Wypisz ilość utworzonych wniosków dla każdego dnia od 20.01.2018,
-- wraz z sumą kroczącą w kolejnych dniach.
-- Dołącz tabelę z wygenerowanymi datami, aby mieć dni do końca lutego.
--
-- Użyj funkcji coalesce do obsługi wartości brakujących (wstaw 0) i left join.

with wnioski_w_dniu as (
   select to_char(data_utworzenia, 'YYYY-MM-DD') :: date data_wniosku, count(1) ilosc_wnioskow
   from wnioski
   where data_utworzenia > '2018-01-20'
   group by 1
   order by 1
),
wygenerowane_daty as (
   select generate_series('2018-01-20'::date, '2018-02-28'::date, '1 day')::date as wygenerowana_data
),
ilosc_rzeczywista_wnioskow as (
   select w1.wygenerowana_data, coalesce(w2.ilosc_wnioskow, 0) as ilosc_wnioskow
   from wygenerowane_daty w1
   left join wnioski_w_dniu w2 on w1.wygenerowana_data = w2.data_wniosku
)

select *, sum(ilosc_wnioskow) over(order by wygenerowana_data) as sum_skumulowana
from ilosc_rzeczywista_wnioskow



----------------------------------------------------------------------------
-- Zadanie 7
--
-- Wypisz ilość wniosków dla każdego dnia od 20.01.2018, wraz z sumą kroczącą
-- w kolejnych dniach.
-- Gdy jest dostępna, użyj rzeczywistej ilości wniosków, gdy nie ma informacji
-- o wnioskach w danym dniu użyj prognozy!
--
-- Rozwiązanie: Dołącz tabelę z prognozowaną ilością wniosków dla danego dnia!

with wnioski_w_dniu as (
    select
      to_char(data_utworzenia, 'YYYY-MM-DD')::date data_wniosku,
      count(1) ilosc_wnioskow
    from wnioski
    where data_utworzenia >= '2018-01-20'
    group by 1
    order by 1
),
wygenerowane_daty as (
    select generate_series('2018-01-20'::date,
                           '2018-02-28'::date, '1 day')::date as wygenerowana_data
),
prognoza_dni_tygodnia as (
    select
      to_char(data_wniosku, 'Day') as dzien,
      round(avg(ilosc_wnioskow)) as srednia_ilosc_wnioskow
    from wnioski_w_dniu
    group by 1
    order by 1
),
ilosc_rzeczywista_wnioskow as (
    select
      w1.wygenerowana_data,
      to_char(w1.wygenerowana_data, 'Day') as dzien,
      coalesce(w2.ilosc_wnioskow, 0) as ilosc_wnioskow
    from wygenerowane_daty w1
    left join wnioski_w_dniu w2 on w1.wygenerowana_data = w2.data_wniosku
),
wnioski_z_prognozami as (
    select
      i.wygenerowana_data,
      i.dzien,
      case
        when i.wygenerowana_data <= '2018-02-09' then i.ilosc_wnioskow
        else p.srednia_ilosc_wnioskow
      end ilosc_wnioskow
    from ilosc_rzeczywista_wnioskow i
    join prognoza_dni_tygodnia p on p.dzien = i.dzien
)

select *, sum(ilosc_wnioskow) over(order by wygenerowana_data) as sum_skumulowana
from wnioski_z_prognozami



----------------------------------------------------------------------------
-- Zadanie 8
--
-- Stwórz indeks na kolumnie jezyk i kanal w tabeli wnioski.

CREATE INDEX wnioski_jezyk
ON wnioski (jezyk)

CREATE INDEX wnioski_kanal
ON wnioski (kanal)



----------------------------------------------------------------------------
-- Zadanie 9
--
-- Przygotuj dane do analizy różnic w acceptance rate analiz operatora
-- dla kolejnych kwartałów roku 2017.

with dane_wnioski_2017 as (
  select
    to_char(w.data_utworzenia, 'Q') as kwartal,
    count(1) as wnioski_ocenione,
    count(case when lower(a.status_odp) like 'zaakceptowany%' then a.id end) as wnioski_zaakceptowane
  from wnioski w
  join analiza_operatora a on a.id_wniosku=w.id
  where to_char(w.data_utworzenia, 'YYYY') = '2017'
  group by 1
)

select
  kwartal,
  wnioski_zaakceptowane/wnioski_ocenione::numeric as acceptance_rate
from dane_wnioski_2017



----------------------------------------------------------------------------
-- Zadanie 10
--
-- Ilustracja obliczeń konwersji / funnela.
--
-- (Ponizsze zapytanie juz bylo w innej formie, zadanie 3 z 03_AnalizaDanych2.sql)
--
-- Ile wniosków mamy w bazie?
-- Jaki procent wniosków został oceniony? (tabela analizy_wnioskow)
-- Ile rekompensat wypłacono? (tabela rekompensaty)
-- Jaki procent wniosków został zaakceptowany na etapie analizy (z wszystkich)?
-- Ile procent wniosków dostało rekompensaty (z zaakceptowanych)?

select
  count(w.id) as ilosc_wnioskow,
  count(a.id_wniosku) as ilosc_ocenionych,
  count(a.id_wniosku)/count(w.id)::numeric as procent_ocenionych,
  count(r.id_wniosku) as ilosc_rekompensat,
  count(r.id_wniosku)/count(w.id)::numeric as procent_rekompensat,
  count(r.id_wniosku)/count(case when a.status = 'zaakceptowany' then a.id_wniosku end)::numeric as procent_rekompensat_z_zaakceptowanych
from wnioski w
left join analizy_wnioskow a on w.id = a.id_wniosku
left join rekompensaty r on w.id = r.id_wniosku