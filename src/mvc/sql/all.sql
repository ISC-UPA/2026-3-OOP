Se tiene dos tablas, parecidas a la DB NorthWind:

CREATE TABLE orders (
  orderID int AUTO_INCREMENT PRIMARY KEY,
  employeeID int NOT NULL,
  order_date date NOT NULL,
  CONSTRAINT ord_emp FOREIGN KEY (employeeID) REFERENCES employees (employeeID)  
);

CREATE TABLE order_details (
  orderID int(10) NOT NULL,
  productID int(10) NOT NULL,
  price decimal(12,4) NOT NULL,
  quantity smallint NOT NULL CHECK (quantity > 0),
  PRIMARY KEY (orderID, productID),
  CONSTRAINT ord_det FOREIGN KEY (orderID)   REFERENCES orders (orderID) ON DELETE CASCADE,
  CONSTRAINT det_pro FOREIGN KEY (productID) REFERENCES products (productID)  
);

ALTER TABLE order_details
  ADD CONSTRAINT Ord_det FOREIGN KEY (orderID) REFERENCES orders (orderID),
  ADD CONSTRAINT det_pro FOREIGN KEY (productID) REFERENCES products (productID);

¿Que opcion es la mas viable?

Opcion 1: Llave compuesta
ALTER TABLE orderdetails
  ADD PRIMARY KEY (OrderID,ProductID);

Opcion 2: llave unica  
ALTER TABLE orderdetails
  ADD column odID int AUTO_INCREMENT PRIMARY KEY;


ALTER TABLE orders
  ADD PRIMARY KEY (OrderID),
  ADD KEY Emp_Ord (EmployeeID);

ALTER TABLE orderdetails
  ADD PRIMARY KEY (OrderID,ProductID)
  