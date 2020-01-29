CREATE OR REPLACE FUNCTION insert_ticket()
  RETURNS trigger AS
$BODY$
BEGIN
    INSERT public."TicketStatus"(status,ticket_id)
    Values("waiting", select id from Ticket where id = new.id);
    RETURN NEW;
END;
$BODY$ LANGUAGE plpgsql;  