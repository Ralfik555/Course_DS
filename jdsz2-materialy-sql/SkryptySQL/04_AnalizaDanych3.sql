----------------------------------------------------------------------------
-- Zadanie 1
--
-- Stwórz listę wniosków z 2015 roku, które mają wypłacone rekompensaty.
-- Każdy wiersz listy, powinien zostać wzbogacony o średnią kwotę rekompensaty
-- dla powodu opóźnienia podanego przez operatora (pole: powod_operatora).
-- Wiersze powinne być ponumerowane po dacie utworzenia wniosku.
select row_number() over (order by data_utworzenia) as np,
       to_char(data_utworzenia, 'DD-MM-YYYY'),
       id, opoznienie, powod_operatora, kod_kraju,
       kwota_rekompensaty,
       avg(kwota_rekompensaty) over (partition by powod_operatora) as srednia_kwota_operator
from wnioski
where 1=1
and extract(year from data_utworzenia) = 2015
and lower(stan_wniosku) like 'wyplac%'
order by 1



----------------------------------------------------------------------------
-- Zadanie 2
--
-- Jaka jest mediana kwoty rekompensat dla partnerów?
-- Jaka jest minimalna i maksymalna kwota rekompensat dla partnerów?
select partner,
       percentile_disc(0.5) within group (order by kwota_rekompensaty) as mediana,
       min(kwota_rekompensaty) as minimalna,
       max(kwota_rekompensaty) as maksymalna
from wnioski
group by partner;



----------------------------------------------------------------------------
-- Zadanie 3
--
-- Przygotuj listę zawierającą liczbę wniosków w każdym miesiącu.
-- Dołącz jako ostatni, wiersz z liczbą wszystkich wniosków
with liczba_wnioskow_dla_lat as (
  select to_char(data_utworzenia,'YYYY-MM'), count(1) liczba_wnioskow
  from wnioski
  group by 1
)

select *
from liczba_wnioskow_dla_lat
union
select 'wszystkie', sum(liczba_wnioskow) from liczba_wnioskow_dla_lat;



----------------------------------------------------------------------------
-- Zadanie 4
--
-- Przygotuj listę nowych wniosków, które mają inny podobny wniosek już wypłacony. Struktura listy:
--
-- ID, stan i identyfikator podróży wniosku o statusie nowy
-- ID, stan i identyfikator podróży wniosku o statusie wyplacony
with moje_dane as (
   select w.id, w.stan_wniosku, s.identyfikator_podrozy, w.data_utworzenia
   from wnioski w
   join podroze p ON w.id = p.id_wniosku
   join szczegoly_podrozy s ON p.id = s.id_podrozy
   where stan_wniosku in ('nowy','wyplacony')
   and s.identyfikator_podrozy not like '%--%'
   order by 1
),
lista_podobnych as (
   select md_nowe.id id_nowego, md_nowe.stan_wniosku, md_nowe.identyfikator_podrozy,
          md_wyplacone.id, md_wyplacone.stan_wniosku, md_wyplacone.identyfikator_podrozy
   from moje_dane md_nowe
   join moje_dane md_wyplacone on md_wyplacone.identyfikator_podrozy = md_nowe.identyfikator_podrozy
   where md_nowe.stan_wniosku = 'nowy'
   and md_wyplacone.stan_wniosku = 'wyplacony'
)

select *
from lista_podobnych;