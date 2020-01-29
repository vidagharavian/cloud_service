CREATE OR REPLACE FUNCTION insert_response()
  RETURNS trigger AS
$BODY$
BEGIN
    UPDATE public."TicketStatus"
    SET public."TicketStatus".status = "answer"
END;
$BODY$ LANGUAGE plpgsql;  