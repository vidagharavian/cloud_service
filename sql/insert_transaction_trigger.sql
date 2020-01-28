CREATE TRIGGER insert_transaction()
  after insert
  ON public."Cloud"
  FOR EACH ROW 
  EXECUTE PROCEDURE insert_transaction();