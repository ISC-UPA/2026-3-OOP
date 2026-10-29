use oop;

CREATE TABLE productos (
  productoID int primary key,
  descripcion varchar(40),
  precio decimal(12,2),
  stock smallint
);


--
-- Volcado de datos para la tabla productos
--

INSERT INTO productos (productoID, descripcion, precio, stock) VALUES
(1, 'Chai', 18.0000, 39),
(2, 'Chang', 19.0000, 17),
(3, 'Aniseed Syrup', 10.0000, 13),
(4, 'Chef Anton\'s Cajun Seasoning', 22.0000, 53),
(5, 'Chef Anton\'s Gumbo Mix', 21.3500, 0),
(6, 'Grandma\'s Boysenberry Spread', 25.0000, 120),
(7, 'Uncle Bob\'s Organic Dried Pears', 30.0000, 15),
(8, 'Northwoods Cranberry Sauce', 40.0000, 6),
(9, 'Mishi Kobe Niku', 97.0000, 29),
(10, 'Ikura', 31.0000, 31),
(11, 'Queso Cabrales', 21.0000, 22),
(12, 'Queso Manchego La Pastora', 38.0000, 86),
(13, 'Konbu', 6.0000, 24),
(14, 'Tofu', 23.2500, 35),
(15, 'Genen Shouyu', 15.5000, 39),
(16, 'Pavlova', 17.4500, 29),
(17, 'Alice Mutton', 39.0000, 0),
(18, 'Carnarvon Tigers', 62.5000, 42),
(19, 'Teatime Chocolate Biscuits', 9.2000, 25),
(20, 'Sir Rodney\'s Marmalade', 81.0000, 40),
(21, 'Sir Rodney\'s Scones', 10.0000, 3),
(22, 'Gustaf\'s Knäckebröd', 21.0000, 104),
(23, 'Tunnbröd', 9.0000, 61),
(24, 'Guaraná Fantástica', 4.5000, 20),
(25, 'NuNuCa Nuß-Nougat-Creme', 14.0000, 76),
(26, 'Gumbär Gummibärchen', 31.2300, 15),
(27, 'Schoggi Schokolade', 43.9000, 49),
(28, 'Rössle Sauerkraut', 45.6000, 26),
(29, 'Thüringer Rostbratwurst', 123.7900, 0),
(30, 'Nord-Ost Matjeshering', 25.8900, 10),
(31, 'Gorgonzola Telino', 12.5000, 0),
(32, 'Mascarpone Fabioli', 32.0000, 9),
(33, 'Geitost', 2.5000, 112),
(34, 'Sasquatch Ale', 14.0000, 111),
(35, 'Steeleye Stout', 18.0000, 20),
(36, 'Inlagd Sill', 19.0000, 112),
(37, 'Gravad lax', 26.0000, 11),
(38, 'Côte de Blaye', 263.5000, 17),
(39, 'Chartreuse verte', 18.0000, 69),
(40, 'Boston Crab Meat', 18.4000, 123),
(41, 'Jack\'s New England Clam Chowder', 9.6500, 85),
(42, 'Singaporean Hokkien Fried Mee', 14.0000, 26),
(43, 'Ipoh Coffee', 46.0000, 17),
(44, 'Gula Malacca', 19.4500, 27),
(45, 'Røgede sild', 9.5000, 5),
(46, 'Spegesild', 12.0000, 95),
(47, 'Zaanse koeken', 9.5000, 36),
(48, 'Chocolade', 12.7500, 15),
(49, 'Maxilaku', 20.0000, 10),
(50, 'Valkoinen suklaa', 16.2500, 65),
(51, 'Manjimup Dried Apples', 53.0000, 20),
(52, 'Filo Mix', 7.0000, 38),
(53, 'Perth Pasties', 32.8000, 0),
(54, 'Tourtière', 7.4500, 21),
(55, 'Pâté chinois', 24.0000, 115),
(56, 'Gnocchi di nonna Alice', 38.0000, 21),
(57, 'Ravioli Angelo', 19.5000, 36),
(58, 'Escargots de Bourgogne', 13.2500, 62),
(59, 'Raclette Courdavault', 55.0000, 79),
(60, 'Camembert Pierrot', 34.0000, 19),
(61, 'Sirop durable', 28.5000, 113),
(62, 'Tarte au sucre', 49.3000, 17),
(63, 'Vegie-spread', 43.9000, 24),
(64, 'Wimmers gute Semmelknödel', 33.2500, 22),
(65, 'Louisiana Fiery Hot Pepper Sauce', 21.0500, 76),
(66, 'Louisiana Hot Spiced Okra', 17.0000, 4),
(67, 'Laughing Lumberjack Lager', 14.0000, 52),
(68, 'Scottish Longbreads', 12.5000, 6),
(69, 'Gudbrandsdalsost', 36.0000, 26),
(70, 'Outback Lager', 15.0000, 15),
(71, 'Fløtemysost', 21.5000, 26),
(72, 'Mozzarella di Giovanni', 34.8000, 14),
(73, 'Röd Kaviar', 15.0000, 101),
(74, 'Longlife Tofu', 10.0000, 4),
(75, 'Rhönbräu Klosterbier', 7.7500, 125),
(76, 'Lakkalikööri', 18.0000, 57),
(77, 'Original Frankfurter grüne Soße', 13.0000, 32);
COMMIT;

update productos set stock = 0;
truncate table detalleOrdenes;
truncate table ordenes;








