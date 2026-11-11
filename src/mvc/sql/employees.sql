CREATE TABLE employees (
  employeeID int AUTO_INCREMENT PRIMARY key, 
  last_name varchar(20),
  first_name varchar(10),
  birth_date datetime,
  hire_date datetime
);


INSERT INTO employees (employeeID, last_name, first_name, birth_date, hire_date) VALUES
(1, 'Davolio', 'Nancy', '1968-12-08 00:00:00', '1992-05-01 00:00:00'),
(2, 'Fuller', 'Andrew', '1952-02-19 00:00:00', '1992-08-14 00:00:00'),
(3, 'Leverling', 'Janet', '1963-08-30 00:00:00', '1992-04-01 00:00:00'),
(4, 'Peacock', 'Margaret', '1958-09-19 00:00:00', '1993-05-03 00:00:00'),
(5, 'Buchanan', 'Steven', '1955-03-04 00:00:00', '1993-10-17 00:00:00'),
(6, 'Suyama', 'Michael', '1963-07-02 00:00:00', '1993-10-17 00:00:00'),
(7, 'King', 'Robert', '1960-05-29 00:00:00', '1994-01-02 00:00:00'),
(8, 'Callahan', 'Laura', '1958-01-09 00:00:00', '1994-03-05 00:00:00'),
(9, 'Dodsworth', 'Anne', '1969-07-02 00:00:00', '1994-11-15 00:00:00');



