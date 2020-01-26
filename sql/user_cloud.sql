CREATE or REPLACE VIEW UserCloud (cloud_id ,first_name,last_name,cost_per_day) AS
SELECT public."Cloud".id ,name as first_name ,f_name,cost_per_day
FROM public."Cloud",public."Customer"
WHERE public."Cloud".user_id = public."Customer".id;