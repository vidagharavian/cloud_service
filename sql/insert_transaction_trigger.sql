CREATE TRIGGER insert_transaction_trigger
  after insert
  ON public."Cloud"
  FOR EACH ROW
  EXECUTE PROCEDURE insert_transaction();