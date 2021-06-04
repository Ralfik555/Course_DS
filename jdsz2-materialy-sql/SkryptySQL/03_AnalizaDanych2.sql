----------------------------------------------------------------------------
-- Zadanie 1
--
-- Eksploracja tabeli wnioski i analiza_prawna

-- Ile jest wniosków dla danych lat i partnerów?
select to_char(data_utworzenia, 'YYYY') as rok, partner, count(1)
from wnioski
group by to_char(data_utworzenia, 'YYYY'), partner
order by 1;

-- Ile wniosków to odrzucone? Ile procent stanowią wnioski odrzucone?
select count(id)
from wnioski as ilosc_odrzuconych
where lower(stan_wniosku) like 'odrzucony%';

select count(
        case
          when lower(stan_wniosku) like 'odrzucony%' then id
        end
       )/count(1)::numeric as tyle_procent_to_odrzucone
from wnioski;

-- Jaka jest średnia wartość rekompensat wniosków odrzuconych
-- dla danych lat i partnerów?
select date_part('year', data_utworzenia),
       partner,
       round(avg(kwota_rekompensaty), 2) as srednia_kwota,
       round(avg(kwota_rekompensaty_oryginalna), 2) as srednia_kwota_oryginalna
from wnioski
group by 1, 2
order by 1, 2;


-- Jaka jest średnia ilość dni między datą wysłania
-- a datą odpowiedzi sądu dla analizy prawnej?
select avg(extract(days from data_wyslania_sad-data_odp_sad))
from analiza_prawna;



----------------------------------------------------------------------------
-- Zadanie 2
--
-- Eksploracja tabel wnioski, analiza_operatora, analizy_prawne

-- Wypisz listę wniosków, które mają analizę prawną?
select *
from wnioski w
join analiza_prawna a on w.id=a.id_wniosku;

-- Ile ich jest?
select count(w.id) as liczba_wnioskow_z_analiza_prawna
from wnioski w
join analiza_prawna a on w.id=a.id_wniosku;

-- Ile wniosków ma analizę prawną dla danego partnera?
select w.partner, count(w.id) as liczba_wnioskow_z_analiza_prawna
from wnioski w
join analiza_prawna a on w.id=a.id_wniosku
group by w.partner;

-- Ile wniosków ma analizę operatora?
select count(w.id) as liczba_wnioskow_z_analiza_operatora
from wnioski w
join analiza_operatora a on w.id=a.id_wniosku;

-- Ile wniosków ma analizę operatora w rozbiciu na lata i partnerów?
select date_part('year', w.data_utworzenia) as rok,
       w.partner,
       count(w.id) as liczba_wnioskow_z_analiza_operatora
from wnioski w
join analiza_operatora a on w.id=a.id_wniosku
group by 1, 2
order by 1, 2;

-- Jaka jest średnia kwota rekompensaty dla wniosków, które mają
-- analizę operatora w rozbiciu na partnerów?
select w.partner,
       avg(kwota_rekompensaty_oryginalna) as srednia_kwota_oryginalna,
       avg(kwota_rekompensaty) as srednia_kwota
from wnioski w
join analiza_operatora a on w.id=a.id_wniosku
group by w.partner;



----------------------------------------------------------------------------
-- Zadanie 3
--
-- Eksploracja tabel wnioski, analizy_wnioskow i rekompensaty

-- Jaki % wniosków został oceniony?
select count(w.id) as liczba_wnioskow,
       count(a.id_wniosku) as liczba_ocenionych,
       count(a.id_wniosku)/count(w.id)::numeric as procent_ocenionych
from wnioski w
left join analizy_wnioskow a on w.id = a.id_wniosku;

-- Jaki % wniosków został zaakceptowany po analizie?
select count(w.id) as liczba_wnioskow,
       count(a.id_wniosku) as liczba_ocenionych,
       count(
         case
           when a.status like 'zaakceptowany%' then a.id_wniosku
         end) as liczba_ocenionych_zaakceptowanych,
       count(
         case
           when a.status like 'zaakceptowany%' then a.id_wniosku
         end)/count(w.id)::numeric as procent_ocenionych_zaakceptowanych
from wnioski w
left join analizy_wnioskow a on w.id = a.id_wniosku;

-- Za jaką część wniosków dostajemy rekompensatę?
select count(w.id) as liczba_wnioskow,
       count(r.id_wniosku) as liczba_rekompensat,
       count(r.id_wniosku)/count(w.id)::numeric as procent_rekompensat
from wnioski w
left join rekompensaty r on r.id_wniosku=w.id;

-- *Jaki jest nasz win rate? (procent rekompensat z zaakceptowanych)
select count(r.id_wniosku)
       /
       count(case when a.status like 'zaakceptowany%' then a.id_wniosku end)::numeric as procent_rekompensat_z_zaakceptowanych
from wnioski w
left join analizy_wnioskow a on w.id = a.id_wniosku
left join rekompensaty r on w.id = r.id_wniosku;



----------------------------------------------------------------------------
-- Zadanie 4
--
-- Jaki jest średni czas od daty wyjazdu do daty złożenia wniosku
-- dla danego języka?
select w.jezyk, date_part('day',avg(w.data_utworzenia - s.data_wyjazdu))
from wnioski w
join podroze p on w.id = p.id_wniosku
join szczegoly_podrozy s on p.id = s.id_podrozy
group by w.jezyk;

-- Ile jest przeterminowanych wniosków (podróż dawniej niż 1000 dni
-- od daty zgłoszenia)?
select count(1)
from wnioski w
join podroze p on w.id = p.id_wniosku
join szczegoly_podrozy s on p.id = s.id_podrozy
where date_part('day', w.data_utworzenia-s.data_wyjazdu) > 1000


-- Ilu klientów podróżowało w celach biznesowych? Ile rekompensat otrzymali?
select count(k.id)
from wnioski w
join klienci k on w.id = k.id_wniosku
where w.typ_podrozy like 'biz%'

select count(1)
from wnioski w
where lower(w.stan_wniosku) like 'wyplacony%'
and lower(w.typ_podrozy) like 'biznes%';


-- Jak szybko (średnia w dniach) klienci biznesowi zgłaszają wnioski
-- po podróży (data wyjazdu)?
select avg(date_part('days', w.data_utworzenia-s.data_wyjazdu))
from wnioski w
join podroze p on w.id = p.id_wniosku
join szczegoly_podrozy s on p.id = s.id_podrozy
where w.typ_podrozy like 'biznes%';



----------------------------------------------------------------------------
-- Zadanie 5
--
-- Jakie są wszystkie kombinacje dla statusu i status
-- sądowego w analizie prawnej (CROSS JOIN)?

select distinct a1.status, a2.status_sad from analiza_prawna a1
cross join analiza_prawna a2
order by 1, 2

-- Czy możesz otrzymać te wyniki inaczej? Na pewno?
select distinct status, status_sad
from analiza_prawna -- niestety to niepelna lista!!!



----------------------------------------------------------------------------
-- Zadanie 6
--
-- Przegląd tabel analiza_operatora i analiza_prawna

-- Znajdź ID wniosków, które zostały poddane analizie prawnej
-- lub analizie operatora

select w.id
from wnioski w
join analiza_operatora a on w.id = a.id_wniosku
union
select w.id
from wnioski w
join analiza_prawna a on w.id = a.id_wniosku;

-- Znajdź ID wniosków, które zostały poddane analizie operatora
-- ale nie analizie prawnej

select w.id
from wnioski w
join analiza_operatora a on w.id = a.id_wniosku
except
select w.id
from wnioski w
join analiza_prawna a on w.id = a.id_wniosku;

-- Znajdź ID wniosków, które zostały poddane analizie prawnej
-- i analizie operatora
select w.id
from wnioski w
join analiza_operatora a on w.id = a.id_wniosku
intersect
select w.id
from wnioski w
join analiza_prawna a on w.id = a.id_wniosku;

select w.id
from wnioski w
join analiza_operatora a on w.id = a.id_wniosku
join analiza_prawna ap on w.id = ap.id_wniosku;



----------------------------------------------------------------------------
-- Zadanie 7
--
-- Wyświetl dane o wnioskach z roku 2018, ponumeruj wiersze oddzielnie
-- dla każdego partnera po datach (użyj ROW_NUMBER OVER()).
-- Posortuj wszystkie wiersze po dacie utworzenia wniosku.
select id, kwota_rekompensaty,
       kwota_rekompensaty_oryginalna,
       row_number() over(partition by partner order by data_utworzenia)
from wnioski
where date_part('year', data_utworzenia) = 2018
order by data_utworzenia;

-- Wyświetl dane o wnioskach, które zostały poddane analizie prawnej,
-- do rezultatu dodaj kolumnę z rankingiem wierszy (funkcja ROW_NUMBER())
-- względem roku utworzenia wniosku
select a.status,
       a.status_sad,
       w.kwota_rekompensaty,
       row_number() over(partition by extract(year from w.data_utworzenia))
from analiza_prawna a
join wnioski w on w.id = a.id_wniosku



----------------------------------------------------------------------------
-- Zadanie 8
--
-- Wyswietl dane o zmianie MoM (month over month) liczby wnioskow
-- w roku 2017
select extract(month from w.data_utworzenia) as miesiac,
       count(1) as biezacy,
       lag(count(1)) over() as poprzedni,
       round(
         1.0*(count(1)-lag(count(1)) over())
           /
              lag(count(1)) over()
         ,3 ) as zmiana
from wnioski w
where extract(year from w.data_utworzenia) = 2017
group by extract(month from w.data_utworzenia)
order by 1



----------------------------------------------------------------------------
-- Zadanie 9
--
-- Analiza kwoty rekompensaty i kwoty rekompensaty oryginalnej
-- w tabeli wnioski

-- Podaj medianę i kwartyle (Q1 i Q3)
select percentile_disc(0.25) within group (order by kwota_rekompensaty) as Q1
from wnioski;

select percentile_disc(0.75) within group (order by kwota_rekompensaty) as Q3
from wnioski;

select percentile_disc(0.25) within group (order by kwota_rekompensaty_oryginalna) as Q1
from wnioski;

select percentile_disc(0.75) within group (order by kwota_rekompensaty_oryginalna) as Q3
from wnioski;

-- Podaj medianę i kwartyle (Q1 i Q3) dla partnerów
select partner,
       unnest(
         percentile_disc(array[0.25,0.5,0.75])
             within group (order by kwota_rekompensaty)
           ) as kwartyle_rekompensata,
       unnest(
         percentile_disc(array[0.25,0.5,0.75])
             within group (order by kwota_rekompensaty_oryginalna)
           ) as kwartyle_rekompensata_oryg,
       unnest(array[0.25,0.5,.75]) as kwartyle
from wnioski
group by partner;



----------------------------------------------------------------------------
-- Zadanie 10
--
-- Analiza korelacji


-- Jaka jest korelacja między kwotą rekompensaty
-- i liczbą pasażerów dla partnerów?
select corr(w.kwota_rekompensaty_oryginalna, liczba_pasazerow),
       partner
from wnioski w
group by w.partner;

-- Jaka jest korelacja między różnicą kwot rekompensat
-- i liczbą pasażerów dla partnerów?
select corr(abs(w.kwota_rekompensaty_oryginalna-w.kwota_rekompensaty), liczba_pasazerow),
       partner
from wnioski w
group by w.partner;