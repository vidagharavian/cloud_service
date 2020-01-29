CREATE OR REPLACE FUNCTION insert_transaction()
  RETURNS trigger AS
$BODY$
BEGIN
    INSERT public."Transaction"(amount,wallet_id)
    VALUES(new.cost_per_day, select id from Wallet where public."Wallet".user_id = new.user_id);
    RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;  