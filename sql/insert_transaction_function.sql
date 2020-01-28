CREATE OR REPLACE FUNCTION insert_transaction()
  RETURNS trigger AS
$BODY$
BEGIN
    INSERT public."Transaction"(amount,wallet_id)
    Values(cost_per_day, select id from Wallet where user_id = new.user_id)
END;
$BODY$ LANGUAGE plpgsql;  