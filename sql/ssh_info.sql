CREATE or REPLACE VIEW SSHInfo (id ,name,public_key,cloud_name,cloud_id,user_id) AS
SELECT public."SSH".id ,name,key  ,host_name,public."Cloud".id,public."SSH".user_id
FROM public."SSH",public."Cloud"
WHERE public."SSH".cloud_id = public."Cloud".id ;