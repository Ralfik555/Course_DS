----------------------------------------------------------------------------
-- Zadanie 7
--
-- Tworzenie tabel i dodawanie rekordów

-- Poniższy kod usuwa tabelki! Odkomentuj jeżeli będzie potrzebny...
-- DROP TABLE IF EXISTS customers CASCADE;
-- DROP TABLE IF EXISTS orders CASCADE;
-- DROP TaBLE IF EXISTS products CASCADE;


-- Tworzenie tabeli customers
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(100)
);

-- Tworzenie tabeli products
CREATE TABLE products (
  product_id INT PRIMARY KEY ,
  product_name VARCHAR(100)
);

-- Tworzenie tabeli orders, realizuje ona zwiazek wiele do wiele
-- miedzy tabelami customers i products
CREATE TABLE orders (
  customer_id INT,
  product_id INT,
  amount INT,
  order_date DATE DEFAULT current_date,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Dodawanie przykładowych wierszy do bazy danych
INSERT INTO customers (customer_id, customer_name) VALUES (1, 'ANNA');
INSERT INTO customers (customer_id, customer_name) VALUES (2, 'KATARZYNA');


-- Dodawanie wielu wierszy na raz, jedyne co potrzebujemy to oddzielić wartości
-- dla kolejnych wierszy przecinkiem
INSERT INTO customers (customer_id, customer_name) VALUES (3, 'JAN'), (4, 'ADAM');

INSERT INTO products (product_id, product_name) VALUES (1, 'PAPIER'),
                                                       (2, 'KAMIEN'),
                                                       (3, 'NOZYCE');

INSERT INTO orders (customer_id, product_id, amount) VALUES (1, 1, 1),
                                                            (1, 2, 10),
                                                            (2, 2, 200);

INSERT INTO orders (customer_id, product_id, amount) VALUES (3, 1, 1), (4, 3, 1);


-- Wypisanie zawartości bazy danych
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM customers;
