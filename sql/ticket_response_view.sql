CREATE or REPLACE VIEW getTicketInfo(ticket_id,response_id,responser_id,ticket_title,
                    ticket_body,response_body,cloud_id,ticket_date_created) AS
SELECT tic.id,res.id,res.responser_id,tic.title,tic.body,res.body,tic.cloud_id,tic.date_created
FROM public."Ticket" tic , public."TicketResponse" res
WHERE tic.id = res.ticket_id