CREATE TRIGGER check_cost()
  after insert
  ON public."Cloud"
  FOR EACH ROW 
  EXECUTE PROCEDURE delete_cloud();