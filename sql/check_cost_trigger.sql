CREATE TRIGGER check_cost()
  after insert
  ON public."Cloud"
  EXECUTE PROCEDURE delete_cloud();