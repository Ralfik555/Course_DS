----------------------------------------------------------------------------
-- Zadanie 2
--
-- Eksploracja tabeli wnioski
select * from wnioski;

select id, kwota_rekompensaty from wnioski;
select id, kwota_rekompensaty, partner from wnioski limit 10;

-- Ilość wniosków w bazie
select count(*) from wnioski;
select count(1) from wnioski;

-- Ilość wniosków z niepustym polem partner
select count(partner) from wnioski;


----------------------------------------------------------------------------
-- Zadanie 3
--
-- Wnioski, dla których zmieniła się wartość rekompensaty

-- Najpierw zobaczmy kilka przykładowych wierszy
select id, kwota_rekompensaty_oryginalna, kwota_rekompensaty
from wnioski
limit 10;

-- Zapytanie, wybierajace tylko wnioski z roznymi kwotami rekompensat
select id, kwota_rekompensaty_oryginalna - kwota_rekompensaty as roznica
from wnioski
where kwota_rekompensaty_oryginalna - kwota_rekompensaty != 0
order by 2 desc;



----------------------------------------------------------------------------
-- Zadanie 4
--
-- Poszukiwane są wnioski, dla których wartość rekompensat na pasażera
-- są różne niż 250, 400 lub 600. Ile ich jest?

-- Najpierw wypiszmy wnioski z informacją o kwocie rekompensat
-- i liczbą pasażerów
select id, kwota_rekompensaty, liczba_pasazerow
from wnioski
limit 10;

-- Wyliczmy kwotę rekompensaty na jednego pasażera
select id,
       kwota_rekompensaty,
       liczba_pasazerow,
       kwota_rekompensaty/liczba_pasazerow as kwota_na_pasazera
from wnioski
limit 10;

-- Rozwiązując zadanie, ostatecznie wypiszmy wnioski, dla których kwota
-- dla pasażera jest różna niż 250, 400 lub 600
select id,
       kwota_rekompensaty,
       liczba_pasazerow,
       kwota_rekompensaty/liczba_pasazerow as kwota_na_pasazera
from wnioski
where kwota_rekompensaty/liczba_pasazerow not in (250, 400, 600);

-- Policzmy ile mamy takich wniosków
select count(id) as liczba_wnioskow
from wnioski
where kwota_rekompensaty/liczba_pasazerow not in (250, 400, 600);



----------------------------------------------------------------------------
-- Zadanie 5
--
-- Użycie GROUP BY w eksploracji tabeli wnioski.

-- Ile wniosków jest w danej kategorii opóźnienia?
select opoznienie, count(1)
from wnioski
group by opoznienie;

-- Ile wniosków zgłoszono w danym roku-miesiącu? (YYYY-MM)
select to_char(data_utworzenia, 'YYYY-MM'), count(1)
from wnioski
group by to_char(data_utworzenia, 'YYYY-MM')
order by 1

-- Ile wniosków jest w danym stanie ?
select stan_wniosku, count(1)
from wnioski
group by stan_wniosku;

-- Wypisz listę stanów wniosków, tylko dla stanów z więcej niż 5000 wniosków.
select stan_wniosku, count(1)
from wnioski
group by stan_wniosku
having count(1) > 5000;



----------------------------------------------------------------------------
-- Zadanie 6
--
-- Eksploracja tabeli wnioski. Użycie funkcji MIN, MAX, AVG, komenda CASE.


-- Ile wniosków ma różne kwoty rekompensat?
select count(
        case
           when kwota_rekompensaty_oryginalna<>kwota_rekompensaty then id
        end) as liczba_roznych
from wnioski;

-- Jaki procent wniosków ma różne kwoty rekompensat?
select count(
        case
           when kwota_rekompensaty_oryginalna<>kwota_rekompensaty then id
        end)/count(1)::numeric as procent_roznych
from wnioski;

-- Jaka jest minimalna, maksymalna i średnia różnica między
-- kwotami rekompensat?
select min(abs(kwota_rekompensaty-kwota_rekompensaty_oryginalna)) as min_roznica,
       max(abs(kwota_rekompensaty-kwota_rekompensaty_oryginalna)) as max_roznica,
       avg(abs(kwota_rekompensaty-kwota_rekompensaty_oryginalna)) as avg_roznica
from wnioski
where kwota_rekompensaty_oryginalna<>kwota_rekompensaty;
