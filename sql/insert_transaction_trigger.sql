CREATE TRIGGER insert_transaction()
  after insert
  ON public."Cloud"
  EXECUTE PROCEDURE insert_transaction();