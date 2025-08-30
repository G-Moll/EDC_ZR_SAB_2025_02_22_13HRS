USE digistore;

-- Query 1
SELECT COUNT( * )
FROM Makers;

SELECT COUNT( * )
FROM Products;


-- Query 2
SELECT
	Makers.name,
	COUNT( Products.id ) AS "Total de Productos"
FROM Makers
	LEFT JOIN Products
	ON Products.maker_id = Makers.id
GROUP BY
	Makers.id
ORDER BY
	2 DESC
-- 	Makers.name ASC
;



SELECT
	Products.id,
	Products.name,
	Products.price,
	Products.maker_id,
-- 	Makers.id,
	Makers.name
FROM Makers
	JOIN Products
	ON Products.maker_id = Makers.id
WHERE
-- 	Products.maker_id = 5
-- 	Makers.name = "Seagate"
	Products.price >= 150
-- 	Makers.name LIKE "S%"
;


-- Query 3
SELECT
	Makers.name,
	MAX( Products.price ) AS "MAXIMO",
	MIN( Products.price ) AS "MINIMO",
	AVG( Products.price ) AS "PROMEDIO"
FROM Makers
	LEFT JOIN Products
	ON Makers.id = Products.maker_id
GROUP BY Makers.id;


-- Query 4
SELECT
	Makers.name AS "MAKER",
	MAX( Products.price ) AS "MAX PRICE",
	MIN( Products.price ) AS "MIN PRICE",
	AVG( Products.price ) AS "AVG PRICE",
	COUNT( * ) AS "UNIDADES"
FROM Products
	LEFT JOIN Makers
	ON Products.maker_id = Makers.id
GROUP BY Makers.id
	HAVING AVG( Products.price ) > 200
-- 	HAVING MAX( Products.price ) < 240
;



SELECT * FROM Makers;
SELECT * FROM Products ;


