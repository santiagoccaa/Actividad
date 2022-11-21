CREATE database Lista_Omar_Blanco;

create table Comando1(
codigo int(4),
nombre varchar(20) not null,
apellido varchar(25) not null,
cedula int(12) unique not null,
telefono int(10) not null,
primary key(codigo)
);

drop table Comando1;

INSERT into Comando1 (codigo, nombre, apellido, cedula, telefono) values
(4,'Jose', 'Carmona', 1007713201, 1234567891);

INSERT into Comando1 (codigo, nombre, apellido, cedula, telefono) values
(5,'Santiago', 'Contreras', 2023201, 22345691);

INSERT into Comando1 (codigo, nombre, apellido, cedula, telefono) values
(6,'Manuel', 'Mejia', 30011201, 32367891);

select * from Comando1;

select * from Comando1 where cedula = 1007713201;
select * from Comando1 where nombre = 'Santiago';
select * from Comando1 where codigo = 6;
