USE digistore;

-- Query 1
SELECT COUNT( * )
FROM Makers;

SELECT COUNT( * )
FROM Products;


-- Query 2
SELECT
	Makers.name,
	COUNT( Products.id )
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




SELECT * FROM Makers;
SELECT * FROM Products ;


