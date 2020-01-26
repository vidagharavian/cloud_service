CREATE OR REPLACE FUNCTION make_tranaction()
  RETURNS trigger AS
$BODY$
BEGIN
   INSERT INTO wallet(amount,id)
   VALUES(new.amount+(select amount from wallet where id=new.wallet_id),new.wallet_id);
   RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;  