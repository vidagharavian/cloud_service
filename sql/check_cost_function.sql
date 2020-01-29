CREATE OR REPLACE FUNCTION delete_cloud()
  RETURNS trigger AS
$BODY$
BEGIN
    DELETE FROM public."Cloud"
    WHERE cost_per_day > some(SELECT amount FROM public."Cloud",public."Wallet" WHERE public."Cloud".user_id = public."Wallet".user_id) ;
END;
$BODY$ LANGUAGE plpgsql;  