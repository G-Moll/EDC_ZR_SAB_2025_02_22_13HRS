-- 3) Modelo Físico
CREATE DATABASE Editorial;
USE Editorial;

SHOW TABLES;

CREATE TABLE Sucursales(
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    domicilio VARCHAR( 120 ),
    telefono VARCHAR( 15 )
);

CREATE TABLE Empleados(
    rfc INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR( 50 ),
    apellidos VARCHAR( 80 ),
    fecnac DATE,
    fecing DATE,
    telefono VARCHAR( 15 ),

    cod_suc INT UNSIGNED,
    FOREIGN KEY( cod_suc ) REFERENCES Sucursales( codigo )
);

DESCRIBE Sucursales;
DESCRIBE Empleados;
