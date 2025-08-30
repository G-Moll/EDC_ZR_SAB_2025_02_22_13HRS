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

INSERT INTO Products VALUES( NULL, "GeForce GTX Xtrme", 755, 6 );
INSERT INTO Products VALUES( NULL, "Monitor 24 LED Full HD", 202, 1 );
INSERT INTO Products VALUES( NULL, "Monitor 27 LED Full HD", 245.99, 1 );
INSERT INTO Products VALUES( NULL, "Laptop Yoga 520", 599, 2 );
INSERT INTO Products VALUES( NULL, "Laptop IdeaPad 320", 444, 2 );
INSERT INTO Products VALUES( NULL, "Printer HP Deskjet 3720", 59.99, 3 );
INSERT INTO Products VALUES( NULL, "Printer HP Deskjet Pro M26nw", 180, 3 );

INSERT INTO Products VALUES( NULL, "Laptop ThinkPad 410T", 800, 2 );
INSERT INTO Products VALUES( NULL, "Printer HP Deskjet Pro M26nw Laser", 800, 3 );
INSERT INTO Products VALUES( NULL, "Monitor 32 LED Full 4k", 810.99, 1 );

SELECT * FROM Products;



