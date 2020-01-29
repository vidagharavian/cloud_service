CREATE TRIGGER insert_ticket_trigger
  after insert
  ON public."Ticket"
  FOR EACH ROW 
  EXECUTE PROCEDURE insert_ticket();