CREATE or REPLACE VIEW CustomerInfo (customer_id ,first_name,last_name,wallet_amount,email) AS
SELECT public."Customer".id ,name as first_name ,f_name,amount,email
FROM public."Wallet",public."Customer"
WHERE public."Wallet".user_id = public."Customer".id;