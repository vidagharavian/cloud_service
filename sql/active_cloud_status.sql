CREATE OR REPLACE FUNCTION active_cloud()
  RETURNS trigger AS
$BODY$
BEGIN
    UPDATE public."Cloud"
    SET public."Cloud".status = "active";
END;
$BODY$ LANGUAGE plpgsql;  