CREATE TRIGGER Chang_wallet_amount
  after insert
  ON public."Transaction"
  FOR EACH ROW
  EXECUTE PROCEDURE make_tranaction();