SHOW DATABASES;
DROP DATABASE digistore;

CREATE DATABASE digistore;
USE digistore;
SHOW TABLES;

CREATE TABLE Makers(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR( 100 ) NOT NULL
);

CREATE TABLE Products(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR( 100 ) NULL NULL,
	price DOUBLE NOT NULL,
	
	maker_id INT UNSIGNED NOT NULL,
	FOREIGN KEY( maker_id ) REFERENCES Makers( id )
);

DESCRIBE Makers;
DESCRIBE Products;


INSERT INTO Makers VALUES( NULL, "Asus" );
INSERT INTO Makers VALUES( NULL, "Lenovo" );
INSERT INTO Makers VALUES( NULL, "HP" );
INSERT INTO Makers VALUES( NULL, "Samsung" ),
	( NULL, "Seagate" ),
	( NULL, "Crucial" ),
	( NULL, "Gigabyte" ),
	( NULL, "Huawei" ),
	( NULL, "Xiaomi" )
;


-- 

SELECT * FROM Makers;
SELECT name, id FROM Makers;

SELECT name, id
FROM Makers
WHERE id >= 7
;

SELECT name, id
FROM Makers
WHERE id >= 3 AND id <= 7
;


SELECT
	name, id
FROM
	Makers
WHERE
	id >= 3 AND id <= 7 AND name LIKE "S%"
;
--


SELECT * FROM Makers;
SELECT * FROM Products;
INSERT INTO Products VALUES( NULL, "Hard disk SATA3 1GB", 86.99, 5 );
INSERT INTO Products VALUES( NULL, "RAM Memory DDR4 8GB", 120, 6 );
INSERT INTO Products VALUES( NULL, "Drive SSD 1TB", 150.99, 4 );
INSERT INTO Products VALUES( NULL, "GeForce GTX 1050Ti", 185, 7 );



