create database oop;

use oop;

create table peajes (
id int auto_increment primary key,
nombre varchar(30),
tipo varchar(10),
placa  varchar(10),
llegada datetime,
montoPeaje decimal
);

insert into peajes values(
null, "Norte", "Carro", "C2", now(), 10000);

insert into peajes(nombre, tipo, placa, llegada,  montoPeaje)
values("Norte","Carro", "C1", now(), 5000);


