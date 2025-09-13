USE school;

DELIMITER //

CREATE TRIGGER tbi_check_note BEFORE INSERT ON Students
    FOR EACH ROW
    BEGIN
        IF NEW.note < 0 THEN
            SET NEW.note = 0;
        ELSEIF NEW.note > 10 THEN
            SET NEW.note = 10;
        END IF;
    END;
    
CREATE TRIGGER tbu_check_note BEFORE UPDATE ON Students
    FOR EACH ROW
    BEGIN
        IF NEW.note < 0 THEN
            SET NEW.note = 0;
        ELSEIF NEW.note > 10 THEN
            SET NEW.note = 10;
        END IF;
    END;//
    
DELIMITER ;
    
SHOW TRIGGERS;
