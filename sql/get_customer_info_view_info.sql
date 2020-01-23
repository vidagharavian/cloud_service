CREATE or REPLACE VIEW Get_customer_info (customer_id,first_name,wallet_amount,last_name)AS
  SELECT public."Customer".id ,name , amount,f_name
  FROM public."Wallet",public."Customer"
  WHERE public."Wallet".user_id = public."Wallet".id;