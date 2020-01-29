CREATE TRIGGER insert_response_trigger
  after insert
  ON public."TicketResponse"
  FOR EACH ROW 
  EXECUTE PROCEDURE insert_response();