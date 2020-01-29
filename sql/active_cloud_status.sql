CREATE OR REPLACE FUNCTION active_cloud()
  RETURNS trigger AS
$BODY$
BEGIN
    SET public."Cloud".status = "active" where public."Cloud".id=new.id;
    return null
END;
$BODY$ LANGUAGE plpgsql;  
