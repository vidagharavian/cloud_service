CREATE OR REPLACE FUNCTION make_wallet()
  RETURNS trigger AS
$BODY$
BEGIN
   INSERT INTO wallet(amount,user_id)
   VALUES(0,new.id);
   RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;  