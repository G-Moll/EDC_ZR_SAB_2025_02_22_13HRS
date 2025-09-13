SHOW DATABASES;
-- DROP DATABASE school;
CREATE DATABASE school;
USE school;

CREATE TABLE Students(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR( 100 ) NOT NULL,
    middlename VARCHAR( 100 ) NOT NULL,
    lastname VARCHAR( 100 ) NOT NULL,
    note DECIMAL NOT NULL
);


SHOW TABLES;
-- DESCRIBE Students;
-- SHOW CREATE TABLE Students;

INSERT INTO Students VALUES( NULL, "Joshua", "Gómez", "Torres", -10 );
INSERT INTO Students VALUES( NULL, "Joshua", "Gómez", "Torres", 18 );
INSERT INTO Students VALUES( NULL, "Joshua", "Gómez", "Torres", -200 );
INSERT INTO Students VALUES( NULL, "Joshua", "Gómez", "Torres", 200 );

INSERT INTO Students VALUES
    ( NULL, "Peter", "Alcántar", "Flores", -1 ),
    ( NULL, "Peter", "Alcántar", "Flores", -20 ),
    ( NULL, "Peter", "Alcántar", "Flores", 11 ),
    ( NULL, "Peter", "Alcántar", "Flores", 18 );

UPDATE Students SET note = 18 WHERE id = 1;
UPDATE Students SET note = -18 WHERE id = 2;
UPDATE Students SET note = 18 WHERE id = 3;

SELECT * FROM Students;