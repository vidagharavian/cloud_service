CREATE or REPLACE VIEW OsOsVersion (os_id ,os_version_id,number,name) AS
SELECT public."OS".id ,public."OsVersion".id ,number,name
FROM public."OS",public."OsVersion"
WHERE public."OsVersion".os_id = public."OS".id;