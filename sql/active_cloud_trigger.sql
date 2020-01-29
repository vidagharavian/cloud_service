CREATE TRIGGER active_cloud_trigger
  after insert
  ON public."Cloud"
  FOR EACH ROW 
  EXECUTE PROCEDURE active_cloud();