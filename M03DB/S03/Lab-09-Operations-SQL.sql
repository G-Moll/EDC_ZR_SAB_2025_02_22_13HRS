USE digistore;

-- Query 1
SELECT name
FROM Products;


-- Query 2
SELECT name, price
FROM Products;


-- Query 3
SELECT *
FROM Products;


-- Query 4
-- Investigar el id del fabricante: 1, 2, 3, etc...
-- Ese id, sirve para filtrar productos de cada fabricante
SELECT *
FROM Products
WHERE maker_id = (SELECT id
	FROM Makers
	WHERE name = "Lenovo")
;



-- Query 5
SELECT * FROM Products WHERE price >= (SELECT MAX( price )
	FROM Products
	WHERE Products.maker_id = (SELECT id
		FROM Makers
		WHERE name = "lenovo")
);


-- Query 6
SELECT Products.name, Products.price
FROM Makers
JOIN Products
ON Makers.id = Products.maker_id
WHERE Makers.name = "LENOVO"  AND Products.price = (SELECT MAX( price )
-- WHERE Makers.name = "HP"  AND Products.price = (SELECT MAX( price )
-- WHERE Products.price >= (SELECT MAX( price )
FROM Makers
	JOIN Products
	ON Makers.id = Products.maker_id
WHERE Makers.name = "LENOVO")
;


-- SELECT
-- FROM
-- WHERE;


SELECT * FROM Products;




